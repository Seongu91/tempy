
<script>
  // Extensions
  import View from '@/views/View'

  // Mixins
  import LoadSections from '@/mixins/load-sections'

  export default {
    name: 'Reference',

    metaInfo: { title: 'Reference' },

    extends: View,

    mixins: [
      LoadSections([
        '404',
        'about-our-product',
        'affiliates',
        'contact-us',
        'features',
        'hero',
        'hero-alt',
        'info',
        'keep-in-touch',
        'map',
        'newsletter',
        'pro-features',
        'social-media',
        'theme-features',
      ]),
    ],

    props: {
      id: {
        type: String,
        default: 'home',
      },
    },
  }
</script>
