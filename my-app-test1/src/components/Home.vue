<template>
    <v-app-bar app color="white" class="d-flex justify-center">
      <div class="d-flex" style="width: 960px">
        <!-- LOGO -->
        
        <v-toolbar-title class="mr-2 headline black--text text--darken-3">
          <span class="font-weight-light">Firmware Analysis Website</span>
          <span></span>
        </v-toolbar-title>
        
        <v-spacer></v-spacer>
  
        <!-- 搜索框 
        <v-text-field
          v-model="searchParam"
          class="mr-4"
          style="max-width: 450px"
          dense
          flat
          hide-no-data
          hide-details
          label="搜索博客"
          append-icon="mdi-magnify"
          @click:append="searchByParam"
          solo-inverted
        ></v-text-field>
        -->
  
        <!-- 导航链接 -->
        <v-btn to="/" text>
          <span class="subtitle-1 black--text text--darken-2">Home</span>
        </v-btn>
        <v-btn to="/Notfound" text>
          <span class="subtitle-1 black--text text--darken-2">CFG</span>
        </v-btn>
        <v-btn to="/BinaryUpload" text>
          <span class="subtitle-1 black--text text--darken-2">Upload&Analysis</span>
        </v-btn>

        <!--
        <v-btn @click="goToGitHub" text>
          <v-icon class="grey--text text--darken-2"> mdi-github </v-icon>
        </v-btn>
        -->
      </div>
    </v-app-bar>
  </template>
  
  <script>
  export default {
    name: "Home",
  
    data() {
      return {
        searchParam: "",
      };
    },
  
    methods: {
      searchByParam() {
      },
      goToGitHub() {
          window.location.href ="https://gitee.com/noissues/tinyblog-vue-vuetify.git";
      },
    },
  };
  </script>
  
  <style>
  .navitem {
    width: 960px;
  }
  </style>
  