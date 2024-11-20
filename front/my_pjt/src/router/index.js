import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import SavingView from '@/views/SavingView.vue'
import depositView from '@/views/depositView.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'
import MapView from '@/views/MapView.vue'
import Login from '@/components/Login.vue';
import Posts from '@/components/Posts.vue';
import MyProfile from '@/components/MyProfile.vue';
import EditProfile from '@/components/EditProfile.vue';
import Signup from '@/components/Signup.vue'
import DetailView from '@/views/DetailView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage,
    },
    {
      path: '/saving',
      name: 'saving',
      component: SavingView,
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: depositView,
    },
    {
      path:'/exchange_rate',
      name:'exchange_rate',
      component:ExchangeRateView
    },
    {
      path:'/detail',
      name:'detail',
      component:DetailView,
      props:true},
    {
      path:'/map',
      name:'map',
      component:MapView
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/signup',
      name: 'signup',
      component: Signup,
    },
    {
      path:'/posts',
      name:'posts',
      component:Posts
    },
    {
      path:'/profile',
      name:'profile',
      component:MyProfile
    },
    {
      path: '/profile/edit',
      name: 'editProfile',
      component:EditProfile
    },
  ],
})

export default router
