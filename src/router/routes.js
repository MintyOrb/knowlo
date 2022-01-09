
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
    ]
  },
  {
    path: '/e',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/explore.vue') }
    ]
  },
  {
    path: '/r',
    name: 'r',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/resourcePage.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
