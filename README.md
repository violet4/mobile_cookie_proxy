# mobile_cookie_proxy
Transfer web/session/login cookies to your phone or other device.

To successfully transfer cookies, it requires that you have the ability to insert DNS requests and make website certificates that your device will trust.

By creating a temporary DNS entry and essentially spoofing the site, you can inject your session cookies into your device, then clear the temporary DNS entry and shut down the server, and your session/login cookies should transfer to the target site.

I wrote this because I'm trying to log into a site from my phone that isn't able to log into that site, but my desktop is already logged in.

Suggested organizational structure:
* `web/auth/mobile_cookie_proxy`
* For gentoo/portage: `net-misc/mobile_cookie_proxy`
