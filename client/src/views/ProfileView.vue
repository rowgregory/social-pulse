<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="col-span-1">
      <Profile :user="user" :friends="friends" />
    </div>
    <div class="col-span-2 space-y-4">
      <PostBox :posts="posts" :user="user" />
      <Posts :posts="posts" />
    </div>
    <div class="col-span-1 space-y-4">
      <PeopleYouMayKnow />
      <Trends />
    </div>
  </div>
</template>

<script>
import PostBox from '@/components/feed/PostBox.vue'
import Profile from '@/components/feed/Profile.vue'
import Posts from '@/components/feed/Posts.vue'
import PeopleYouMayKnow from '@/components/feed/PeopleYouMayKnow.vue'
import Trends from '@/components/feed/Trends.vue'
import axios from 'axios'

export default {
  name: 'ProfileView',
  components: {
    PostBox,
    Profile,
    Posts,
    PeopleYouMayKnow,
    Trends,
  },
  data() {
    return {
      posts: [],
      user: {},
      friends: [],
    }
  },
  mounted() {
    this.getMyPosts()
  },
  watch: {
    '$route.params.id': {
      handler: function () {
        this.getMyPosts()
      },
      deep: true,
      immediate: true,
    },
  },
  methods: {
    getMyPosts() {
      axios
        .get(`/api/posts/${this.$route.params.id}`)
        .then((res) => {
          console.log('PROFILE FEED: ', res.data)
          this.posts = res.data.posts
          this.user = res.data.user
          this.friends = res.data.friends
        })
        .catch((err) => console.log('ERROR: ', err))
    },
  },
}
</script>
