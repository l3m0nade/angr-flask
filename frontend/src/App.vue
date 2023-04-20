<!-- App.vue is the first vue template the vuerify check. As the base and global part-->
<template>
  <v-app>
    <!-- 
    //this part will give an mobile navigation bar on the left.no need now
    <v-navigation-drawer app>
    </v-navigation-drawer>
    -->
    <v-app-bar app color="white" class="d-flex justify-center">
        <div class="d-flex" style="width: 960px">
        <!-- LOGO -->
        
        <v-toolbar-title class="d-flex mr-2 headline black--text text--darken-3">
          <span class="font-weight-light">Firmware Analysis Website</span>
          <span></span>
        </v-toolbar-title>
        
        <v-spacer></v-spacer>
  
        <!-- 导航链接 -->
        <v-btn to="/" text>
          <span class="subtitle-1 black--text text--darken-2">Home</span>
        </v-btn>
        <v-btn to="/cfg" text>
          <span class="subtitle-1 black--text text--darken-2">CFG</span>
        </v-btn>
        <v-btn to="/BinaryUpload" text>
          <span class="subtitle-1 black--text text--darken-2">Upload&Analysis</span>
        </v-btn>
        </div>
        
    </v-app-bar>

  <!-- Sizes your content based upon application components -->
  <v-main>

    <!-- Provides the application the proper gutter -->
    <v-container fluid>
      <!--
      <v-shell
      :banner="banner"
      :shell_input="send_to_terminal"
      :commands="commands"
      @shell_output="prompt">

      </v-shell>
      -->
      <!--
      <v-card v-for="(output, index) in outputs" :key="index>
        <v-card-header>
          Output {{ index + 1 }}
        
        <v-card-body>
          <pre>{{ output }}</pre>
        
      <v-card/>-->
      <!-- If using vue-router -->
      <router-view></router-view>
    </v-container>
  </v-main>

  <v-footer>
    <!--no need-->
  </v-footer>

    <!--
      if you do like this,because youhave import Homevue below,
      the dom has make once,you will get this made twice
    <Home />
    -->
    

    <!--
    <div>
    <h1>Binary Processor aaa</h1>
    <div class="container">
      <form @submit.prevent="processBinary" class="form-inline">
        <div class="form-group">
          <input type="file" ref="binary" class="form-control-file">
        </div>
        <button type="submit" class="btn btn-primary">Process</button>
      </form>
    </div>
    <div class="container">
      <div class="card" v-for="(output, index) in outputs" :key="index">
        <div class="card-header">
          Output {{ index + 1 }}
        </div>
        <div class="card-body">
          <pre>{{ output }}</pre>
        </div>
      </div>
    </div>
    </div>
    -->

    
  </v-app>
</template>

<script>
import Home from './components/Home';

export default {
  name: 'App',

  components: {
    Home,
  },

  data(){
    return {
      stdoutData: ''
    }
  },
  methods: {
  },
  
};
</script>
<!--
<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Firmware Binary Analysis Tool</v-toolbar-title>
    </v-app-bar>
    
    <v-main>
      <v-container fluid>
        <v-slide-y-transition>
          <v-layout justify-center>
            <v-flex xs12 sm8 md6>
              <v-card>
                <v-card-title class="headline text-center">File Uploader</v-card-title>
                <v-divider></v-divider>
                <v-card-text>
                  <component :is="currentTab"></component>
                </v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-slide-y-transition>
      </v-container>
    </v-main>
  </v-app>

  
</template>
-->
