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
          Binary CFG
        </v-btn>
      </v-form>
      
      <v-img :src="imageSrc"></v-img>

    </v-container>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'CFG',
    data () {
      return {
        selectedFile: null,
        imageSrc: '',
        loading: false,
        filename:null,
      }
    },
    mounted() {
    this.getImage();
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
      onSubmit () {
        let formData = new FormData()
        this.filename = this.selectedFile.name
        console.log(this.filename)
        formData.append('file', this.selectedFile)
        this.loading = true
        axios.post('http://127.0.0.1:5000/getCFG', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then(response => {
          this.imageSrc = URL.createObjectURL(new Blob([response.data]));
        }).catch(error => {
          console.error(error);
        }).finally(() => {
        this.loading = false

        
      })
      }
    }
  }
  </script>
  
  