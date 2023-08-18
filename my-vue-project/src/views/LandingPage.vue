<!-- src/views/LandingPage.vue -->

<template>
    <div>
      <LandingOffer />
      <!-- Other sections of your landing page -->
    </div>
  </template>
  
  <script>
  import LandingOffer from '@/components/LandingOffer.vue';
  
  export default {
    components: {
      LandingOffer
    }
  }
  </script>
  