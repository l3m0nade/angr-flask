<template>
  
  <v-card
    class="mx-auto"
    max-width="344"
    outlined
  >
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4">OVERLINE</div>
        <v-list-item-title class="headline mb-1">Headline 5</v-list-item-title>
        <v-list-item-subtitle>Greyhound divisely hello coldly fonwderfully</v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar
        tile
        size="80"
        color="grey"
      ></v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <v-btn text>Button</v-btn>
      <v-btn text>Button</v-btn>
    </v-card-actions>
  </v-card>
  
</template>

  <script>
  export default {
    name: "Home",
  
    data() {
      return {
        searchParam: "",
        items: [
          {
            header: 'Today',
          },
          { divider: true },
          {
            avatar: 'https://picsum.photos/250/300?image=660',
            title: 'Meeting @ Noon',
            subtitle:
              "<span class='font-weight-bold'>Spike Lee</span> &mdash; I'll be in your neighborhood",
          },
          {
            avatar: 'https://picsum.photos/250/300?image=821',
            title: 'Summer BBQ <span class="grey--text text--lighten-1"></span>',
            subtitle:
              "<span class='font-weight-bold'>to Operations support</span> &mdash; Wish I could come.",
          },
          {
            header: 'Yesterday',
          },
          { divider: true },
          {
            avatar: 'https://picsum.photos/250/300?image=1006',
            title: 'Dinner tonight?',
            subtitle:
              "<span class='font-weight-bold'>LaToya</span> &mdash; Do you want to hang out?",
          },
          {
            avatar: 'https://picsum.photos/250/300?image=146',
            title: 'So long',
            subtitle:
              "<span class='font-weight-bold'>Nancy</span> &mdash; Do you see what time it is?",
          },
          {
            header: 'Last Week',
          },
          { divider: true },
          {
            avatar: 'https://picsum.photos/250/300?image=1008',
            title: 'Breakfast?',
            subtitle:
              "<span class='font-weight-bold'>LaToya</span> &mdash; Do you want to hang out?",
          },
          {
            avatar: 'https://picsum.photos/250/300?image=839',
            title:
              'Winter Porridge <span class="grey--text text--lighten-1"></span>',
            subtitle:
              "<span class='font-weight-bold'>cc: Daniel</span> &mdash; Tell me more...",
          },
        ],
      };
    },
  
    methods: {
      searchByParam() {
      },
      goToGitHub() {
          window.location.href ="https://gitee.com/noissues/tinyblog-vue-vuetify.git";
      },
    },
  };
  </script>
  
  <style>
  .navitem {
    width: 960px;
  }
  </style>
  


  <!-- 搜索框 
        <v-text-field
          v-model="searchParam"
          class="mr-4"
          style="max-width: 450px"
          dense
          flat
          hide-no-data
          hide-details
          label="搜索博客"
          append-icon="mdi-magnify"
          @click:append="searchByParam"
          solo-inverted
        ></v-text-field>
        -->

  <!--
        <v-btn @click="goToGitHub" text>
          <v-icon class="grey--text text--darken-2"> mdi-github </v-icon>
        </v-btn>
        -->


  <!--
      <div>
      <v-card max-width="344" class="mx-auto">
        <v-list-item>
          <v-list-item-avatar color="grey"></v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title class="headline">Our Changing Planet</v-list-item-title>
            <v-list-item-subtitle>by Kurt Wagner</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-img src="https://cdn.vuetifyjs.com/images/cards/mountain.jpg" height="194"></v-img>

        <v-card-text>
          Visit ten places on our planet that are undergoing the biggest changes today.
        </v-card-text>

        <v-card-actions>
          <v-btn
            text
            color="deep-purple accent-4"
          >
            Read
          </v-btn>
          <v-btn
            text
            color="deep-purple accent-4"
          >
            Bookmark
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn icon>
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon>mdi-share-variant</v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </div>
    -->


<!--
<v-list two-line>
          <template v-for="(item, index) in items">
            <v-subheader
              v-if="item.header"
              :key="item.header"
              inset
            >
              {{ item.header }}
            </v-subheader>

            <v-divider
              v-else-if="item.divider"
              :key="index"
              inset
            ></v-divider>

            <v-list-item
              v-else
              :key="item.title"
              ripple
              @click=""
            >
              <v-list-item-avatar>
                <img :src="item.avatar">
              </v-list-item-avatar>

              <v-list-item-content>
                <v-list-item-title v-html="item.title"></v-list-item-title>
                <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>
              </v-list-item-content>

            </v-list-item>
          </template>
        </v-list>

-->