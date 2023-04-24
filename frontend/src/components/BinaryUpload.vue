<template>
  
    <v-container fluid>
      <v-form @submit.prevent="onSubmit" ref="fileID" type="file">
        <v-file-input
          v-model="selectedFile"
          label="Select file"
          
          :rules="fileRules"
          outlined
          required
        ></v-file-input>
        <v-btn
          type="submit"
          color="primary"
          :loading="loading"
          :disabled="!valid"
        >
          Upload
        </v-btn>
      </v-form>
      
      <v-card>
      <v-card-title>Output:</v-card-title>
      <v-card-text>{{ output }}</v-card-text>
      </v-card>
      
      
      <div v-for="(file, index) in this.output" :key="index">
        <img :src="`${file}.svg`" />
        <v-divider></v-divider>
      </div>
      
    </v-container>

    
    
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'BinaryUpload',
    data () {
      return {
        selectedFile: null,
        loading: false,
        imageList: [],
        imagePath:null,
        output:null,
      }
    },
    computed: {
      valid () {
        return !!this.selectedFile
      },
      fileRules () {
        return [
          value => {
            if (!value) {
              return 'File is required'
            } 
            return true
          }
        ]
      }
    },
    mounted() {
    this.getData();
    
  },
       
    methods: {
      getData (){
        console.log("getData")
        /*
        files = require.context('@/assets/'+this.imagePath, true, /\.svg$/).keys();
        console.log(files);
        this.imageList = files
        */
      },
      onSubmit () {
        console.log(this.selectedFile.name)
        let formData = new FormData()
        formData.append('file', this.selectedFile)
        this.loading = true
        axios.post('http://127.0.0.1:5000/upload_file', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then(response => {
          //this.output = response.data.result.map(item => ({result: item}));
          this.output = response.data.result
          console.log(this.output);
        })
        .catch(error => {
          console.error(error);
        }).finally(() => {
        this.loading = false
        this.output = this.output.split("\n")
        this.output.pop()
        console.log(this.output)
        
      })
      }
    }
  }
  
</script>  


<!--
  .then(res => {
            Vue.set(this.person,0,{age:res.data.age,name:res.data.name,sex:res.data.sex}))
-->