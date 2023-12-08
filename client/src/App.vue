<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <Navbar />
  <main class="py-8 bg-gray-100">
    <RouterView />
  </main>
  <Toast />
</template>

<script>
import Navbar from './components/Navbar.vue'
import Toast from '@/components/Toast.vue'
import { useUserStore } from '../src/stores/user'
import axios from 'axios'

export default {
  components: {
    Toast,
  },
  beforeCreate() {
    const userStore = useUserStore()
    userStore.initStore()

    const token = userStore.user.access

    if (token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
    } else {
      axios.defaults.headers.common['Authorization'] = ``
    }
  },
}
</script>
