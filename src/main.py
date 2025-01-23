import handler.confighandler as config
import client.pinterestclient as pinclient
import client.bloggerclient as blogclient

config = config.Config()
pin_cl = pinclient.PinterestClient(config)
blog_cl = blogclient.BloggerClient(config)

img_content = pin_cl.get_pin_from_board()
blog_cl.blog(img_content)
pin_cl.delete_pin(img_content.get("id"))