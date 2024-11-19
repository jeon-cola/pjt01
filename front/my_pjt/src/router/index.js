import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import SavingView from '@/views/SavingView.vue'
import depositView from '@/views/depositView.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'
import MapView from '@/views/MapView.vue'
import SignupView from '@/views/SignupView.vue'
import LoginView from '@/views/loginView.vue'


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
      component: SavingView
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: depositView
    },
    {
      path:'/exchange_rate',
      name:'exchange_rate',
      component:ExchangeRateView
    },
    {
      path:'/map',
      name:'map',
      component:MapView
    },
    {
      path:'/signup',
      name:'signup',
      component:SignupView,
      children:[
        {path:'/login',name:'login',component:LoginView}
      ]
    }
  ],
})

export default router
