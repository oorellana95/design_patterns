import logging

from structural.bridge.devices.dslr_camera import dslr_camera
from structural.bridge.devices.webcam import webcam
from structural.bridge.streaming_services.twitch_stream import TwitchStreamingService
from structural.bridge.streaming_services.youtube_stream import YouTubeStreamingService


def main_bridge() -> None:
    # setup logging
    logging.basicConfig(level=logging.INFO)

    # create a device and a streaming service
    service = YouTubeStreamingService()
    service.add_device(webcam)  # The devices are decoupled, they are added individually using "add_device".

    # start streaming
    reference = service.start_stream()
    service.fill_buffer(reference)  # Gets the information inside all added devices.
    service.stop_stream(reference)

    # create another device and streaming service
    service2 = TwitchStreamingService()
    service2.add_device(dslr_camera)
    service2.add_device(webcam)

    # start streaming there as well
    reference2 = service2.start_stream()
    service2.fill_buffer(reference2)
    service2.stop_stream(reference2)
