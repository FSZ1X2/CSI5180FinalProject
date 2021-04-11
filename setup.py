from setuptools import setup

setup(
        name="discordbot",
        packages=["DiscordBot"],
        install_requires=[
		"asyncio",
        	"discord.py",
		"tinydb",
                "apiai"
		], 
        zip_safe=False
)
