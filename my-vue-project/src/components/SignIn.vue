<template>
    <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
      <!-- ... your HTML code ... -->
  
      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" @submit.prevent="signIn">
          <div>
            <label for="username" class="block text-sm font-medium leading-6 text-gray-900">Deposit Number</label>
            <div class="mt-2">
              <input id="username" name="username" type="text" v-model="username" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>
  
          <div>
            <div class="flex items-center justify-between">
              <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
              <div class="text-sm">
                <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
              </div>
            </div>
            <div class="mt-2">
              <input id="password" name="password" type="password" v-model="password" autocomplete="current-password" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>
  
          <div>
            <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign In</button>
          </div>
        </form>
  
        <p class="mt-10 text-center text-sm text-gray-500">
          Not a member?
          {{ ' ' }}
          <router-link to="/signup" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Sign Up</router-link>
        </p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'SignIn',
    data() {
      return {
        username: '', // Username input field value
        password: '', // Password input field value
      };
    },
    methods: {
      async signIn() {
        try {
          const csrfToken = this.getCookie('csrftoken');
          const response = await axios.post(
            `http://localhost:8000/accounts/_login`, // Replace with your login endpoint
            {
              username: this.username,
              password: this.password,
            },
            {
              headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
              },
            }
          );
  
          this.$store.commit('setAuthentication', true);
          
          // Handle successful sign-in (e.g., redirect, show message, etc.)
          console.log('Sign-in successful:', response.data);
  
          // Redirect to dashboard or appropriate route
          this.$router.push('/dashboard'); // Replace with your dashboard route path
        } catch (error) {
          // Handle error (e.g., show error message to user)
          console.error('Error signing in:', error);
        }
      },
      getCookie(name) {
        let value = '; ' + document.cookie;
        let parts = value.split('; ' + name + '=');
        if (parts.length == 2) return parts.pop().split(';').shift();
      },
    },
  };
  </script>
  