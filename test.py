    def on_enter_nintendo-switch(self, event):
        scraper = IgnScraper('nintendo-switch')
        scraper.asyncGetPages()
        titleList = scraper.getTitleLists()
        msg = []
        for index in range(len(titleList)):
            msg.append(scraper.getBasicInfo(titleList[index]['url']))

        reply_token = event.reply_token
        send_text_message(reply_token, msg[random.randint(0, len(msg) - 1)])
        self.go_back()

    def on_exit_nintendo-switch(self):
        print('nintendo-switch leaving')