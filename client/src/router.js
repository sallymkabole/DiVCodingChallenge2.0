import Vue from 'vue';
import Router from 'vue-router';
import Ping from './components/Ping.vue';
import Tasks from './components/Tasks.vue';

Vue.use(Router);

export default new Router({
  mode: 'history', // enable page load without reload
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/tasks',
      name: '/Tasks',
      component: Tasks,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
