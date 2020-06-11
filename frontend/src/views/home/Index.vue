
<script>
  // Extensions
  import View from '@/views/View'

  // Mixins
  // import LoadSections from '@/mixins/load-sections'

  export default {
    name: 'Home',

    metaInfo: { title: 'Home' },

    extends: View,

    props: {
      id: {
        type: String,
        default: 'home',
      },
    },
  }
</script>
