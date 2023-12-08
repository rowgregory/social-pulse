<template>
  <div
    v-if="userStore?.user?.id === user?.id"
    class="bg-white border border-gray-200 rounded-lg"
  >
    <form method="post" v-on:submit.prevent="submitForm">
      <div class="p-4">
        <textarea
          v-model="body"
          class="p-4 w-full bg-gray-100 rounded-lg box-border"
          placeholder="What are you thinking about?"
        ></textarea>
      </div>
      <div class="p-4 border-t border-gray-100 flex justify-between">
        <a
          href="#"
          class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg"
          >Attach</a
        >
        <button
          href="#"
          class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg"
        >
          Post
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'

export default {
  name: 'PostBox',
  props: {
    user: {
      type: Object,
    },
  },
  created() {
    console.log('THIS USER: ', this.user)
  },
  setup() {
    const userStore = useUserStore()
    return { userStore }
  },
  data() {
    return {
      posts: [],
      body: '',
    }
  },
  methods: {
    submitForm() {
      console.log('SUBMIT FORM', this.body)

      axios
        .post('/api/posts/create/', { body: this.body })
        .then((res) => {
          console.log('POST CREATE')
          this.posts.unshift(res.data)
          this.body = ''
        })
        .catch((err) => {
          console.log('POST CREATE ERR: ', err)
        })
    },
  },
}
</script>
