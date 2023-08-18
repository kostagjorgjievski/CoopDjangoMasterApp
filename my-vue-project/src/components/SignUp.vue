
<template>

  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company" />
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign up your account</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" @submit.prevent="register">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
          <div class="mt-2">
            <input id="email" name="email" type="email" v-model="email" autocomplete="email" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
          </div>
        </div>

        <div>
        <label for="username" class="block text-sm font-medium leading-6 text-gray-900">Username</label>
        <div class="mt-2">
            <input id="username" name="username" type="text" v-model="username" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
        </div>
    </div>

    <div>
        <label for="first_name" class="block text-sm font-medium leading-6 text-gray-900">First Name</label>
        <div class="mt-2">
            <input id="first_name" name="first_name" type="text" v-model="first_name" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
        </div>
    </div>

    <div>
        <label for="last_name" class="block text-sm font-medium leading-6 text-gray-900">Last Name</label>
        <div class="mt-2">
            <input id="last_name" name="last_name" type="text" v-model="last_name" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
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
        <label for="password2" class="block text-sm font-medium leading-6 text-gray-900">Confirm Password</label>
        <div class="mt-2">
            <input id="password2" name="password2" type="password" v-model="password2" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
        </div>
    </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign Up</button>
        </div>
      </form>

      <p class="mt-10 text-center text-sm text-gray-500">
        Already a member?
        {{ ' ' }}
        <router-link to="/signin" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Sign In</router-link>
      </p>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
export default {
  name: 'SignUp',
  data() {
    return {
      email: '',
      username: '',
      first_name: '',
      last_name: '',
      password: '',
      password2: ''
    };
  },
  methods: {
    getCookie(name) {
    let value = "; " + document.cookie;
    let parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
  },
    async register() {
      try {
        const csrfToken = this.getCookie('csrftoken');
        console.log(this.username)
        const response = await axios.post(`http://localhost:8000/accounts/register`, {
          email: this.email,
          username: this.username,
          first_name: this.first_name,
          last_name: this.last_name,
          password: this.password,
          password2: this.password2
          // ... any other fields you have ...
        },{
        headers: {
          'X-CSRFToken': csrfToken,
          'Content-Type': 'application/json'
          }
        });

        // Handle successful registration (e.g., redirect, show message, etc.)
        console.log('Registration successful:', response.data);
        this.$router.push('/signin');
      } catch (error) {
        // Handle error (e.g., show error message to user)
        console.error('Error registering:', error);
      }
    }
  }
};
</script>
