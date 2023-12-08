import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '../views/SignUpView.vue'
import SignInView from '../views/SignInView.vue'
import FeedView from '../views/FeedView.vue'
import ProfileView from '../views/ProfileView.vue'
import SearchView from '../views/SearchView.vue'
import FriendsView from '../views/FriendsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignInView,
    },
    {
      path: '/feed',
      name: 'feed',
      component: FeedView,
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView,
    },
    {
      path: '/profile/:id/friends',
      name: 'friends',
      component: FriendsView,
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
  ],
})

export default router
