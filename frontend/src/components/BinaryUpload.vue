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

      <v-data-table ref="MyTable" :headers="analysis" :items="output"></v-data-table>

      
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
        output:null,
        analysis:[
          {
            text: 'Result', value: 'result'
          }
        ],
        headers:[
        {
          result: 'Name123',
          
        }
      ],

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
    methods: {
      getResult (){
        axios.get("http://127.0.0.1:5000/getjson")
      },
      onSubmit () {
        let formData = new FormData()
        formData.append('file', this.selectedFile)
        this.loading = true
        axios.post('http://127.0.0.1:5000/upload_file', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then(response => {
          this.output = response.data.result.map(item => ({result: item}));
          console.log(this.output);
        }).catch(error => {
          console.error(error);
        }).finally(() => {
        this.loading = false

        
      })
      }
    }
  }
  
</script>  