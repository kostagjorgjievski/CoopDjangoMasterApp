<template>
  <div id="app">
    <LandingNavbar v-if="!computedIsAuthenticated" />

    <div v-if="!computedIsAuthenticated" class="flex justify-center items-center min-h-screen">
      <router-view></router-view>
    </div>
    <div v-else>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

import LandingNavbar from './components/LandingNavbar.vue';

export default {
  components: {
    LandingNavbar,
  },
  setup() {
    const store = useStore();

    // Compute the value of isAuthenticated based on the store state
    const computedIsAuthenticated = computed(() => {
      return store.state.isAuthenticated;
    });

    return {
      computedIsAuthenticated
    };
  }
};
</script>

<style>
/* Add your styles here */
</style>
