<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title color="indigo">
          <span class="headline">Input Event Info</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field v-model="eventTitle" label="title" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-textarea v-model="eventDescription" label="description" row-height="24px"></v-textarea>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  type="datetime-local"
                  label="start"
                  v-model="eventStart"
                  step="900"
                  required
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  type="datetime-local"
                  label="end"
                  step="900"
                  v-model="eventEnd"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-btn small @click="submitEvent()">Done</v-btn>
            <v-btn small @click="close()">Cancel</v-btn>
          </v-container>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import api from "../services/api";

export default {
  data() {
    return {
      dialog: false,
      eventTitle: "",
      eventDescription: "",
      eventStart: null,
      eventEnd: null
    };
  },
  methods: {
    open() {
      this.dialog = true;
    },
    close() {
      this.dialog = false;
    },
    submitEvent() {
      const event = {
        title: this.eventTitle,
        description: this.eventDescription,
        start_at: this.eventStart,
        end_at: this.eventEnd
      };
      api
        .post("events/", event)
        .then(res => console.log(res))
        .catch(err => console.log(err));
      this.eventTitle = "";
      this.eventDescription = "";
      this.eventStart = null;
      this.eventEnd = null;

      this.dialog = false;
    }
  }
};
</script>
