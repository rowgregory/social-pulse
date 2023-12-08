<template>
  <nav class="py-6 px-8 border-b border-gray-200">
    <div class="flex items-center justify-between mx-auto w-full">
      <div class="menu-left">
        <a href="#" class="text-xl">Social Pulse</a>
      </div>
      <div class="grid grid-cols-1 lg:grid-cols-4 gap-12">
        <RouterLink to="/feed" class="text-purple-700">
          <Home />
        </RouterLink>
        <a href="#">
          <Message />
        </a>
        <a href="#"><Notifications /> </a>
        <RouterLink to="/search"><Search /> </RouterLink>
      </div>
      <div class="menu-right">
        <template v-if="userStore?.user?.isAuthenticated">
          <RouterLink
            v-if="userStore && userStore.user && userStore.user.id"
            :to="{
              name: 'profile',
              params: { id: userStore?.user?.id },
            }"
          >
            <img src="https://i.pravatar.cc/40?img=70" class="rounded-full" />
          </RouterLink>
        </template>
        <template v-else>
          <RouterLink
            to="/signin"
            class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg"
            >Sign in</RouterLink
          >
          <RouterLink
            to="/signup"
            class="py-4 px-6 bg-purple-600 text-white rounded-lg"
            >Sign up</RouterLink
          >
        </template>
      </div>
    </div>
  </nav>
</template>

<script>
import { useUserStore } from '@/stores/user'
import Home from '@/assets/svg/Home.vue'
import Message from '@/assets/svg/Message.vue'
import Notifications from '@/assets/svg/Notifications.vue'
import Search from '@/assets/svg/Search.vue'
import { RouterLink } from 'vue-router'

export default {
  components: { Home, Message, Notifications, Search, RouterLink },
  setup() {
    const userStore = useUserStore()
    console.log('USERSTORE USER: ', userStore.user)
    return { userStore }
  },
}
</script>
