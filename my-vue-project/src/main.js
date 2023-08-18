
import './assets/css/main.css'
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from '../store/store'; // Adjust the path as needed



createApp(App).use(store).use(router).mount('#app');

