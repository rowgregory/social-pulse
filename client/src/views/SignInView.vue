<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="p-12 bg-white border border-gray-200 rounded-lg">
      <h1 class="m-0 text-gray-500">Sign In</h1>
      <p class="font-bold">
        Don't have an account?
        <RouterLink :to="{ name: 'signup' }" class="underline"
          >Click here</RouterLink
        >
        to sign up!
      </p>
    </div>

    <div class="p-12 bg-white border border-gray-200 rounded-lg">
      <form class="space-y-6" v-on:submit.prevent="submitForm">
        <div class="flex flex-col">
          <label>Email</label>
          <input
            v-model="form.email"
            type="email"
            placeholder="Enter email address"
            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
          />
        </div>
        <div class="flex flex-col">
          <label>Password</label>
          <input
            v-model="form.password"
            type="password"
            placeholder="Enter your password"
            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
          />
        </div>
        <template v-if="errors.length > 0">
          <div class="bg-red-300 text-white rounded-lg p-6">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
        </template>
        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">
          Sign In
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast'
import { useUserStore } from '@/stores/user'

export default {
  setup() {
    const toastStore = useToastStore()
    const userStore = useUserStore()

    return {
      toastStore,
      userStore,
    }
  },
  data() {
    return {
      form: {
        email: '',
        password: '',
      },
      errors: [],
    }
  },
  methods: {
    async submitForm() {
      this.errors = []

      if (this.form.email === '') {
        this.errors.push('Email is missing')
      }
      if (this.form.password === '') {
        this.errors.push('Password is missing')
      }

      if (this.errors.length === 0) {
        await axios
          .post('/api/signin/', this.form)
          .then((response) => {
            console.log('SUCCESS LOGIN', response.data)
            this.userStore.setToken(response.data)

            axios.defaults.headers.common[
              'Authorization'
            ] = `Bearer ${response.data.access}`
          })
          .catch((err) => {
            console.log('ERROR: ', err)
          })

        await axios
          .get('/api/foryou/')
          .then((response) => {
            console.log('SUCCESS ME', response.data)
            this.userStore.setUserInfo(response.data)

            this.$router.push('/feed')
          })
          .catch((err) => {
            console.log('ERROR ME: ', err)
          })
      }
    },
  },
}
</script>
