"""Player chat event"""
import json
from discord import Embed, Color
from .registry import Registry
from ..event import EventProcessor, Event


class ServerStartStopEventProcessor(EventProcessor):
    """Processes server start and stop events."""
    
    event_types = ["server_start", "server_stop"]
        
    async def process_event(self, event: Event) -> None:
        """
        Process the server start or stop event.
        
        Args:
            event: The event to process.
        """
        
        embed = Embed(            color=Color.green() if event.event_type == "server_start" else Color.red(),
        )
        embed.set_author(name="Server | " + ("Started" if event.event_type == "server_start" else "Stopped"))
        
        await self.context.notifier.send_embed(embed)
        
        self.context.logger.info(f"Processed server start/stop event: {event.event_type}")
        
# Register the event processor
Registry.add(ServerStartStopEventProcessor)