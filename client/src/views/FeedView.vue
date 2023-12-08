<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="col-span-3 space-y-4">
      <PostBox :user="user" />
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
import Posts from '@/components/feed/Posts.vue'
import PeopleYouMayKnow from '@/components/feed/PeopleYouMayKnow.vue'
import Trends from '@/components/feed/Trends.vue'
import axios from 'axios'

export default {
  name: 'FeedView',
  components: {
    PostBox,
    Posts,
    PeopleYouMayKnow,
    Trends,
  },
  data() {
    return {
      posts: [],
      user: {},
    }
  },
  mounted() {
    this.getFeed()
  },

  methods: {
    getFeed() {
      axios
        .get('/api/posts/')
        .then((res) => {
          console.log('FEED RES: ', res.data)
          this.posts = res.data.posts
          this.user = res.data.user
        })
        .catch((err) => console.log('ERROR: ', err))
    },
  },
}
</script>
