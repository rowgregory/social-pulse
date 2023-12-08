<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="p-12 bg-white border border-gray-200 rounded-lg">
      <h1 class="m-0 text-gray-500">Sign up</h1>
      <p class="font-bold">
        Already have an account?
        <RouterLink :to="{ name: 'signin' }" class="underline"
          >Click here</RouterLink
        >
        to sign in!
      </p>
    </div>

    <div class="p-12 bg-white border border-gray-200 rounded-lg">
      <form class="space-y-6" v-on:submit.prevent="submitForm">
        <div class="flex flex-col">
          <label>Name</label>
          <input
            v-model="form.name"
            type="text"
            placeholder="Enter name"
            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
          />
        </div>
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
            v-model="form.password1"
            type="password"
            placeholder="Enter your password"
            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
          />
        </div>
        <div class="flex flex-col">
          <label>Confirm Password</label>
          <input
            v-model="form.password2"
            type="password"
            placeholder="Confirm your password"
            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
          />
        </div>
        <template v-if="errors.length > 0">
          <div class="bg-red-300 text-white rounded-lg p-6">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
        </template>
        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">
          Sign Up
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast'

export default {
  setup() {
    const toastStore = useToastStore()

    return {
      toastStore,
    }
  },
  data() {
    return {
      form: {
        email: '',
        name: '',
        password1: '',
        password2: '',
      },
      errors: [],
    }
  },
  methods: {
    submitForm() {
      this.errors = []

      if (this.form.name === '') {
        this.errors.push('Name is missing')
      }
      if (this.form.email === '') {
        this.errors.push('Email is missing')
      }
      if (this.form.password1 === '') {
        this.errors.push('Password is missing')
      }
      if (this.form.password2 === '') {
        this.errors.push('Passwords do not match')
      }

      if (this.errors.length === 0) {
        axios
          .post('/api/signup/', this.form)
          .then((response) => {
            if (response.data.message === 'success') {
              this.toastStore.showToast(
                5000,
                'The user is registered. Please log in.',
                'bg-emerald-400'
              )

              this.form.email = ''
              this.form.name = ''
              this.form.password1 = ''
              this.form.password2 = ''
            } else {
              this.toastStore.showToast(
                5000,
                'Oops! Something went wrong. Please try again.',
                'bg-red-300'
              )
            }
          })
          .catch((err) => {
            console.log('ERROR: ', err)
          })
      }
    },
  },
}
</script>
