// store.js
import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      isAuthenticated: false,
    };
  },
  mutations: {
    setAuthentication(state, status) {
      state.isAuthenticated = status;
    },
  },
});

export default store;
