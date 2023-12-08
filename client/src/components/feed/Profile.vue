<template>
  <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
    <img
      src="https://i.pravatar.cc/500?img=68"
      class="mb-6 rounded-full w-full"
    />
    <p>{{ user.name }}</p>
    <div class="mt-6 flex space-x-8 justify-around">
      <RouterLink
        :to="{ name: 'friends', params: { id: user.id } }"
        class="text-sm text-gray-500"
        ><p>
          {{ user.friends_count }} friend{{
            user.friends_count === 1 ? '' : 's'
          }}
        </p></RouterLink
      >
      <p class="text-sm text-gray-500">120 posts</p>
    </div>
    <div class="mb-6" v-if="showFriendRequestButton">
      <button
        @click="sendFriendRequest"
        class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg text-sm"
      >
        Send friend request
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { ref, watchEffect } from 'vue'

export default {
  props: {
    user: { type: Object },
    friends: { type: Array },
  },
  setup(props) {
    const userStore = useUserStore()
    const friends = ref(props.friends)
    watchEffect(() => {
      friends.value = props.friends
    })

    return {
      userStore,
      friends,
    }
  },
  computed: {
    showFriendRequestButton() {
      return (
        // this.userStore.user.id !== this.$route.params.id ||
        !this.friends?.some((friend) => friend.id === this.userStore.user.id)
      )
    },
  },
  methods: {
    async sendFriendRequest() {
      await axios
        .post(`/api/friends/request/${this.$route.params.id}`)
        .then((res) => {
          console.log('SEND FRIEND REQUEST RESPONSE: ', res.data)
        })
        .catch((err) => {
          console.log('ERROR SEND FRIEND REQUEST: ', err)
        })
    },
  },
  components: { RouterLink },
}
</script>
