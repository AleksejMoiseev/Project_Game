from publisherkombu import connection, video_queue, process_media


with connection.Consumer([video_queue],
                         callbacks=[process_media]) as consumer:
    while True:
        connection.drain_events()
