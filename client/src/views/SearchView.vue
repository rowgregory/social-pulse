<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-3 space-y-4">
      <div class="bg-white border border-gray-200 rounded-lg">
        <form v-on:submit.prevent="submitForm" class="p-4 flex space-x-4">
          <input
            v-model="query"
            type="search"
            class="p-4 w-full bg-gray-100 rounded-lg"
            placeholder="What are you looking for?"
          />

          <button
            class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg"
          >
            Search
          </button>
        </form>
      </div>

      <div
        v-if="users.length > 0"
        class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4"
      >
        <div
          v-for="user in users"
          v-bind:key="user?.id"
          class="p-4 text-center bg-gray-100 rounded-lg"
        >
          <img
            src="https://i.pravatar.cc/300?img=70"
            class="mb-6 rounded-full w-full"
          />

          <p>
            <strong>
              <RouterLink
                :to="{
                  name: 'profile',
                  params: { id: user?.id },
                }"
              >
                {{ user?.name }}</RouterLink
              ></strong
            >
          </p>

          <div class="mt-6 flex space-x-8 justify-around">
            <p class="text-xs text-gray-500">182 friends</p>
            <p class="text-xs text-gray-500">120 posts</p>
          </div>
        </div>
      </div>
      <div class="main-left col-span-3 space-y-4">
        <Posts :posts="posts" />
      </div>
    </div>
    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />
      <Trends />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '@/components/feed/PeopleYouMayKnow.vue'
import Trends from '@/components/feed/Trends.vue'
import Posts from '@/components/feed/Posts.vue'

export default {
  name: 'SearchView',
  components: {
    PeopleYouMayKnow,
    Trends,
    Posts,
  },
  data() {
    return {
      query: '',
      users: [],
      posts: [],
    }
  },
  methods: {
    submitForm() {
      if (!this.query) {
        this.posts = []
        this.users = []

        return
      }
      axios
        .get(`/api/search/${this.query}`)
        .then((res) => {
          console.log('SEARCH RES: ', res.data)
          this.users = res.data.users
          this.posts = res.data.posts
        })
        .catch((err) => console.log('SEARCH ERR: ', err))
    },
  },
}
</script>
