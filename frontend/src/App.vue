<template>
  <div id="app">
    <v-app>
      <v-app-bar app color="indigo">
        <v-toolbar-title>Calendar</v-toolbar-title>
      </v-app-bar>
      <v-content>
        <v-container class="fill-height">
          <v-row>
            <v-col justify="center">
              <router-view />
            </v-col>
          </v-row>
        </v-container>
      </v-content>
    </v-app>
  </div>
</template>