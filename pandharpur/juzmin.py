JAZZMIN_SETTINGS = {
    "site_title": "Pandharpur Admin",
    "site_header": "Pandharpur",
    "site_brand": "Pandharpur Management",
    "site_logo": "favicon/logo.png",  # Fixed path issue
    "site_logo_classes": "img-circle",
    "custom_css": "css/custom_admin.css",  # Custom CSS for animations & responsiveness
    "custom_js": "js/custom_admin.js",  # Optional: Add JS for animations if needed
    "site_icon": "favicon/favicon.ico",  # Add favicon if available
    "welcome_sign": "Welcome to the Pandharpur Management",
    "copyright": "Pandharpur Management",
    "search_model": "auth.User",
    "user_avatar": None,

    # Top Navigation Menu
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "", "new_window": True},
        {"model": "auth.User"},
        {"app": "books"},
    ],

    # User Menu (Top Right Dropdown)
    "usermenu_links": [
        {"name": "Support", "url": "", "new_window": True},
        {"model": "auth.user"},
    ],

    # Sidebar Menu
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Custom Links in Sidebar
    "custom_links": {
        "books": [{
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Sidebar Icons
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # UI & Animations
    "related_modal_active": False,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
}
