<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="col-span-1">
      <Profile :user="user" />
    </div>
    <div class="col-span-2 space-y-4">
      <div
        v-if="friendRequests.length"
        class="p-4 bg-white border border-gray-200 rounded-lg grid gap-4"
      >
        <h2 class="text-gray-900">Friend Requests</h2>
        <div
          v-for="user in friendRequests"
          v-bind:key="user.id"
          class="p-4 text-center bg-gray-100 rounded-lg"
        >
          <img
            src="https://i.pravatar.cc/300?img=70"
            class="mx-auto mb-6 rounded-full w-3/12"
          />

          <p>
            <strong>
              <RouterLink
                :to="{
                  name: 'profile',
                  params: { id: user?.created_by?.id },
                }"
              >
                {{ user.created_by.name }}</RouterLink
              ></strong
            >
          </p>

          <div class="mt-6 flex space-x-8 justify-around">
            <p class="text-xs text-gray-500">182 friends</p>
            <p class="text-xs text-gray-500">120 posts</p>
          </div>
          <div class="mt-6 flex justify-center gap-4">
            <button
              @click="handleFriendRequest('accepted', user.created_by.id)"
              class="inline-block py-4 px-6 bg-green-600 text-white rounded-lg text-sm"
            >
              Accept
            </button>

            <button
              @click="handleFriendRequest('rejected', user.created_by.id)"
              class="inline-block py-4 px-6 bg-red-600 text-white rounded-lg text-sm"
            >
              Reject
            </button>
          </div>
        </div>
      </div>
      <div
        v-if="friends.length"
        class="p-4 bg-white border border-gray-200 rounded-lg grid gap-4 grid-cols-2"
      >
        <div
          v-for="friend in friends"
          v-bind:key="friend.id"
          class="p-4 text-center bg-gray-100 rounded-lg"
        >
          <img
            src="https://i.pravatar.cc/300?img=70"
            class="mx-auto mb-6 rounded-full w-3/12"
          />

          <p>
            <strong>
              <RouterLink
                :to="{
                  name: 'profile',
                  params: { id: friend?.id },
                }"
              >
                {{ friend.name }}</RouterLink
              ></strong
            >
          </p>

          <div class="mt-6 flex space-x-8 justify-around">
            <p class="text-xs text-gray-500">
              {{ friend.friends_count }} friend{{
                friend.friends_count > 1 || friend.friends_count === 0
                  ? 's'
                  : ''
              }}
            </p>
            <p class="text-xs text-gray-500">120 posts</p>
          </div>
        </div>
      </div>
    </div>
    <div class="col-span-1 space-y-4">
      <PeopleYouMayKnow />
      <Trends />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '@/components/feed/PeopleYouMayKnow.vue'
import Trends from '@/components/feed/Trends.vue'
import Profile from '@/components/feed/Profile.vue'

export default {
  name: 'FriendsView',
  components: {
    PeopleYouMayKnow,
    Profile,
    Trends,
  },
  data() {
    return {
      user: {},
      friends: [],
      friendRequests: [],
    }
  },
  mounted() {
    this.getFriends()
  },
  methods: {
    getFriends() {
      axios
        .get(`/api/profile/${this.$route.params.id}/friends/`)
        .then((res) => {
          console.log('GET FRIENDS RESPONSE: ', res.data)
          this.friendRequests = res.data.requests
          this.friends = res.data.friends
          this.user = res.data.user
        })
        .catch((err) => {
          console.log('ERROR GETTING FRIENDS: ', err)
        })
    },
    handleFriendRequest(status, pk) {
      console.log('STATUS: ', status)
      axios
        .post(`/api/friends/${pk}/${status}`)
        .then((res) => {
          console.log('HANDLE FRIEND REQUEST RESPONSE: ', res.data)
        })
        .catch((err) => {
          console.log('ERROR GETTING FRIENDS: ', err)
        })
    },
  },
}
</script>
