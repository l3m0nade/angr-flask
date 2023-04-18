import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import("@/components/Home.vue")
      
    },
    {
      path: '/binaryupload',
      name: 'BinaryUpload',
      component: () => import("@/components/BinaryUpload.vue")
    },
    {
      path: '*',
      component: () => import("@/components/Notfound.vue")
    }
  ]
})