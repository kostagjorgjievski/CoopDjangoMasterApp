import { createRouter, createWebHistory } from 'vue-router';

// Your component imports here
import LandingPage from './views/LandingPage.vue';
import SignUp from '@/components/SignUp.vue';
import SignIn from '@/components/SignIn.vue';
import AppDashboard from '@/views/AppDashboard.vue'

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp,
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: SignIn,
  },
  {
    path: '/dashboard',
    name: 'AppDashboard',
    component: AppDashboard,
  }
  // ... other routes
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
