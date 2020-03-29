import Vue from 'vue';
import Router from 'vue-router';
import Ping from './components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history', // enable page load without reload
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
