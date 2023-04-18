from angr import Project
from angr.knowledge_plugins.key_definitions.constants import OP_BEFORE
from angr.analyses.reaching_definitions.dep_graph import DepGraph
import os
from pathlib import Path
from networkx.drawing.nx_agraph import write_dot
from angr.knowledge_plugins.key_definitions.tag import ReturnValueTag,InitialValueTag
from angr.analyses.reaching_definitions.function_handler import FunctionHandler
from angr.knowledge_plugins.key_definitions.atoms import Register

def magic_graph_print(folder,filename, dependency_graph):
    path_and_filename = "/home/l3m0nade/Desktop/Code/angr-iot/angr-iot2/angr-iot/output/%s/%s"%(folder,filename)
    print(path_and_filename)
    write_dot(dependency_graph, "%s.dot" % path_and_filename)
    os.system("dot -Tsvg -o %s.svg %s.dot" % (path_and_filename, path_and_filename))
    os.system("rm -rf /home/l3m0nade/Desktop/Code/angr-iot/angr-iot2/angr-iot/output/%s/*.dot"%folder)





class myHandler(FunctionHandler):
    def __init__(self,project,cfg,function_address) -> None:
        self.state = None
        self.codeloc = None
        self._analysis = None
        self.function_address = function_address
        self.cfg = cfg
        self.project = project
        self.predecessors = None
    
    def hook(self,rda):
        self._analysis = rda
        return self
    
    def handle_local_function(
        self,
        state,
        function_address,
        call_stack,
        maximum_local_call_depth,
        visited_blocks,
        dep_graph,
        src_ins_addr,
        codeloc,
    ):
        """
        :param state: The state at the entry of the function, i.e. the function's input state.
        :param function_address: The address of the function to handle.
        :param call_stack:
        :param maximum_local_call_depth:
        :param visited_blocks: A set of the addresses of the previously visited blocks.
        :param dep_graph: A definition-use graph, where nodes represent definitions, and edges represent uses.
        :param codeloc: The code location of the call to the analysed function.
        """
        function = self._analysis.project.kb.functions.function(function_address)
        return False, state, visited_blocks, dep_graph
    
    def find_reg_name(self,offset):
        for i in self.project.arch.register_list:
            if offset == i.vex_offset:
                return i.name
        return "None"


    def handle_sprintf(self,state,codeloc):
        # print("handle sprintf !!!")
        # print("current state is {}".format(state))
        self.state = state
        self.codeloc = codeloc

        project = self.project
        reg_names = ["a0","a1","a2","a3"]
        reg_defs = []
        for reg_name in reg_names:
            reg = project.arch.get_register_by_name(reg_name)
            g = state.live_definitions.get_register_definitions(reg.vex_offset,reg.size)
            reg_def = next(g)
            reg_def.tags.add(self.find_reg_name(reg_def.atom.reg_offset))
            reg_defs.append(reg_def)
        # 更新a0 和 几个参数之间的依赖关系
        dst_def = reg_defs[0]
        dst_def.tags.add("sprintf handler")
        for src_def in reg_defs[1:]:
            state.analysis.dep_graph.add_edge(src_def,dst_def)
        # 

        src_def = list(state.live_definitions.register_uses.get_uses_by_insaddr(dst_def.codeloc.ins_addr))[0]
        state.analysis.dep_graph.add_edge(src_def,dst_def)

        return True,state
    
    def handle_snprintf(self,state,codeloc):
        # print("handle sprintf !!!")
        # print("current state is {}".format(state))
        self.state = state
        self.codeloc = codeloc

        project = self.project
        reg_names = ["a0","a2","a3"]
        reg_defs = []
        for reg_name in reg_names:
            reg = project.arch.get_register_by_name(reg_name)
            g = state.live_definitions.get_register_definitions(reg.vex_offset,reg.size)
            reg_def = next(g)
            reg_def.tags.add(self.find_reg_name(reg_def.atom.reg_offset))
            reg_defs.append(reg_def)
        # 更新a0 和 几个参数之间的依赖关系
        dst_def = reg_defs[0]
        dst_def.tags.add("snprintf handler")
        for src_def in reg_defs[1:]:
            state.analysis.dep_graph.add_edge(src_def,dst_def)
        # 

        src_def = list(state.live_definitions.register_uses.get_uses_by_insaddr(dst_def.codeloc.ins_addr))[0]
        state.analysis.dep_graph.add_edge(src_def,dst_def)

        return True,state

    def handle_doSystem(self,state,codeloc):
        # print("handle sprintf !!!")
        # print("current state is {}".format(state))
        self.state = state
        self.codeloc = codeloc

        project = self.project
        reg_defs = []
        # for reg_name in reg_names:
        #     reg = project.arch.get_register_by_name(reg_name)
        #     g = state.live_definitions.get_register_definitions(reg.vex_offset,reg.size)
        #     reg_def = next(g)
        #     reg_def.tags.add(find_reg_name(reg_def.atom.reg_offset))
        #     reg_defs.append(reg_def)
        predecessors = self.cfg.get_node(codeloc.ins_addr).predecessors
        dst_def = None
        for x in predecessors:
            if x.function_address == self.function_address:
                start = x.addr
                end = x.addr + project.factory.block(start).size
                target = []
                target.append(project.arch.get_register_offset("a0"))
                target.append(project.arch.get_register_offset("a1"))
                target.append(project.arch.get_register_offset("a2"))
                target.append(project.arch.get_register_offset("a3"))
                # reg = project.arch.get_register_by_name("a0")
                all_definitions = state.all_definitions
                # source = []
                for y in all_definitions:
                    if y.codeloc.ins_addr and start < y.codeloc.ins_addr < end and type(y.atom) == Register and y.atom.reg_offset in target:
                        if y.tags:
                            y.tags.clear()
                        y.tags.add("reg name is {}".format(self.find_reg_name(y.atom.reg_offset)))
                        if self.find_reg_name(y.atom.reg_offset) == "a0":
                            dst_def = y
                        else:
                            reg_defs.append(y)


        # 更新a0 和 几个参数之间的依赖关系
        dst_def.tags.add("doSystem handler")
        for src_def in reg_defs:
            state.analysis.dep_graph.add_edge(src_def,dst_def)


        return True,state
    

class VunChecker():
    def __init__(self,project,rd_dep_graph):
        self.project = project
        self.rd_dep_graph = rd_dep_graph
    
    def check(self,reg_def):
        def_set = set()
        def_set.add(reg_def)
        source_def = set()
        while len(def_set):
            cur_def = def_set.pop()
            if cur_def.tags:
                def_tag = cur_def.tags.copy()
                t_def = type(def_tag.pop())
                if t_def == ReturnValueTag:
                    source_def.add(cur_def)
            for pred in self.rd_dep_graph.graph.predecessors(cur_def):
                def_set.add(pred)

        return source_def
    

    
def check_function(target,func_name,arg_pos):
    #filename = "./sample/%s"%target
    filename = target
    project = Project(filename,auto_load_libs=False)
    cfg = project.analyses.CFGFast()
    project.analyses.CompleteCallingConventions(recover_variables=True)
    reg_name = project.kb.functions[func_name].calling_convention.ARG_REGS[arg_pos-1]
    # 目标函数地址
    func_addr = project.kb.functions[func_name].addr
    # 获取cfg中目标地址的节点
    func_node = cfg.get_any_node(func_addr)
    # 获取节点的前驱
    func_node_preds = func_node.predecessors
    # 筛选出前驱节点的地址
    func_preds = list(set([i.function_address for i in func_node_preds]))
    # 构建字典，以地址为key
    FUNC_PREDECESSORS = {}

    for func_pred_addr  in func_preds:
        FUNC_PREDECESSORS[hex(func_pred_addr)] = []
    for i in func_node_preds:
        FUNC_PREDECESSORS[hex(i.function_address)].append(i)

    # 遍历所有的节点，对每个节点进行reaching definition analysis，寻找某个参数是否可控
    OVERALL_DEFS = set()
    FUNCS = set()
    # 遍历字典
    for func_pred_addr,xrefs in FUNC_PREDECESSORS.items():
        
        # if func_pred_addr != "0x42264c":
            # continue
        # print("Analyzing predecessor func at {}".format(func_pred_addr))
        func_pred_addr = int(func_pred_addr[2:],16)
        # print("Xrefs are {}".format(xrefs))
        # 遍历所有的 ??
        for xref in xrefs:
            # print("Analyzing xref at {}".format(hex(xref.addr)))
            # 获取function 对象
            func_pred = cfg.functions.get_by_addr(func_pred_addr)

            call_to_xref_addr = project.factory.block(xref.addr).instruction_addrs[-2]

            observation_point = ("insn",call_to_xref_addr,OP_BEFORE)
            
            try:
                # depgraph = DepGraph()
                # handler = myHandler(project,cfg,func_pred.addr)
                rd = project.analyses.ReachingDefinitions(
                    subject = func_pred,
                    func_graph = func_pred.graph,
                    cc = func_pred.calling_convention,
                    observation_points = [observation_point],
                    function_handler = myHandler(project,cfg,func_pred.addr),
                    dep_graph = DepGraph()
                )
                results = rd.observed_results[observation_point]
                reg = project.arch.get_register_by_name(reg_name)
                reg_definition = list(results.get_register_definitions(reg.vex_offset,reg.size))[0]
                checker = VunChecker(project,rd.dep_graph)
                source_defs = checker.check(reg_definition)
                if source_defs:
                    #reg_dependencies = rd.dep_graph.transitive_closure(reg_definition)
                    #magic_graph_print(target,"sub_{}".format(hex(func_pred_addr)[2:]),reg_dependencies)
                    print("possible vunlerable function at sub_{}".format(hex(func_pred_addr)[2:]))
            except Exception as e:
                print("reaching definition error occured")
                print(e)

'''
func_name = "doSystem"
arg_pos = 1
target = "mipsel-bin2"
check_function(target,func_name,arg_pos)

'''