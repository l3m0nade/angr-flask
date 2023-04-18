
<template>
  <v-app>
    <Home />
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

    <v-main>
      <router-view />
    </v-main>
  </v-app>
  
</template>

<script>
import Home from './components/Home';

export default {
  name: 'App',

  components: {
    Home,
  },

  data: () => ({
    //
  }),
  methods:{},
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

<script>
import BinaryUpload from '@/components/BinaryUpload.vue'

export default {
  name: 'App',
  components: {
    BinaryUpload
  },
  data () {
    return {
      drawer: false,
      uploadTab: true
    }
  },
  computed: {
    currentTab () {
      return this.uploadTab ? 'BinaryUpload' : null
    }
  }
}
</script>
-->
