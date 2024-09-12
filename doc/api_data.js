define({ "api": [
  {
    "version": "1.0.0",
    "group": "Admin",
    "name": "AdminActivate",
    "type": "post",
    "url": "/v1/admin/activate",
    "title": "Activate a admin user",
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "ttl",
            "description": "<p>TTL of secret key</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "secret_key",
            "description": "<p>Secret key of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "Admin",
            "optional": false,
            "field": "admin",
            "description": "<p>Admin details (<a href=\"#api-Admin-GetAdmin\">admin object</a>)</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/admin/api.py",
    "groupTitle": "Admin",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "code",
            "description": "<p>Activation code for the admin</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>User name of the admin</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Admin",
    "name": "AdminAuthenticate",
    "type": "post",
    "url": "/v1/admin/authenticate",
    "title": "Authenticate a admin user and send activation code",
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Username of the user</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "activate_ttl",
            "description": "<p>Activate token ttl</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/admin/api.py",
    "groupTitle": "Admin",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Admin username</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Admin password (pattern='^[A-Za-z0-9]{5,}$')</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Admin",
    "name": "AdminChangePassword",
    "type": "put",
    "url": "/v1/admin/password",
    "title": "Change admin password",
    "filename": "./application/controllers/v1/admin/api.py",
    "groupTitle": "Admin",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "old_password",
            "description": "<p>Old password of this admin. (pattern='^[A-Za-z0-9]{5,}$')</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "new_password",
            "description": "<p>New password of this admin. (pattern='^[A-Za-z0-9]{5,}$')</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Admin",
    "name": "AdminUpdateProfile",
    "type": "put",
    "url": "/v1/admin/profile",
    "title": "Update admin profile",
    "filename": "./application/controllers/v1/admin/api.py",
    "groupTitle": "Admin",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Admin name</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Admin email</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Id of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Name of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Email of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Username of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "Permission[]",
            "optional": false,
            "field": "permissions",
            "description": "<p>Permissions of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "permissions.name",
            "description": "<p>Name of permission</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "permissions.access_level",
            "description": "<p>Access level of permission (None=0, Read=1, Write=2)</p>"
          },
          {
            "group": "Success Response",
            "type": "Permission[]",
            "optional": true,
            "field": "permissions.sub_permissions",
            "description": "<p>Sub permissions of permission</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Admin",
    "name": "CreateAdmin",
    "type": "post",
    "url": "/v1/admin",
    "title": "Create a admin user",
    "filename": "./application/controllers/v1/admin/api.py",
    "groupTitle": "Admin",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Admin name</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Admin email</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Admin username</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Admin password (pattern='^[A-Za-z0-9]{5,}$')</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Permission[]",
            "optional": false,
            "field": "permissions",
            "description": "<p>Admin permissions</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "permissions.name",
            "description": "<p>Permission name</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": true,
            "field": "permissions.access_level",
            "description": "<p>Permission access level (none=0, read=1, write=2)</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Permission[]",
            "optional": true,
            "field": "permissions.sub_permissions",
            "description": "<p>Sub permission of permissions</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Id of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Name of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Email of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Username of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "Permission[]",
            "optional": false,
            "field": "permissions",
            "description": "<p>Permissions of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "permissions.name",
            "description": "<p>Name of permission</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "permissions.access_level",
            "description": "<p>Access level of permission (None=0, Read=1, Write=2)</p>"
          },
          {
            "group": "Success Response",
            "type": "Permission[]",
            "optional": true,
            "field": "permissions.sub_permissions",
            "description": "<p>Sub permissions of permission</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 201 Created",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Admin",
    "name": "DeleteAdmin",
    "type": "delete",
    "url": "/v1/admin/:username",
    "title": "Delete a admin user",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Admin username</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/admin/api.py",
    "groupTitle": "Admin",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Admin",
    "name": "GetAdmin",
    "type": "get",
    "url": "/v1/admin/:username",
    "title": "Get a admin user",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Admin username</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/admin/api.py",
    "groupTitle": "Admin",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Id of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Name of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Email of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Username of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "Permission[]",
            "optional": false,
            "field": "permissions",
            "description": "<p>Permissions of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "permissions.name",
            "description": "<p>Name of permission</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "permissions.access_level",
            "description": "<p>Access level of permission (None=0, Read=1, Write=2)</p>"
          },
          {
            "group": "Success Response",
            "type": "Permission[]",
            "optional": true,
            "field": "permissions.sub_permissions",
            "description": "<p>Sub permissions of permission</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Admin",
    "name": "GetAdminList",
    "type": "get",
    "url": "/v1/admin",
    "title": "Get admin list",
    "parameter": {
      "fields": {
        "Query Parameter": [
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "query",
            "description": "<p>Filter by query (search in email and username)</p>"
          }
        ],
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Current page</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "per_page",
            "defaultValue": "25",
            "description": "<p>Object per page (per_page = -1 return all)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Admin[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Admin-GetAdmin\">admin object</a></p>"
          }
        ],
        "Success - 2xx": [
          {
            "group": "Success - 2xx",
            "type": "Object",
            "optional": false,
            "field": "meta",
            "description": "<p>Pagination meta data.</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_next",
            "description": "<p>Pagination has next page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.next",
            "description": "<p>Url for next page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_prev",
            "description": "<p>Pagination has previous page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.prev",
            "description": "<p>Url for previous page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.page",
            "description": "<p>Number of the current page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.pages",
            "description": "<p>All pages count</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.per_page",
            "description": "<p>Item per each page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.total",
            "description": "<p>Count of all items</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/admin/api.py",
    "groupTitle": "Admin",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Admin",
    "name": "UpdateAdmin",
    "type": "put",
    "url": "/v1/admin/:username",
    "title": "Update a admin user",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Admin username</p>"
          }
        ],
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Admin name</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Admin email</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Admin password (pattern='^[A-Za-z0-9]{5,}$')</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Permission[]",
            "optional": false,
            "field": "permissions",
            "description": "<p>Admin permissions</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "permissions.name",
            "description": "<p>Permission name</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": true,
            "field": "permissions.access_level",
            "description": "<p>Permission access level (none=0, read=1, write=2)</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Permission[]",
            "optional": true,
            "field": "permissions.sub_permissions",
            "description": "<p>Sub permission of permissions</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/admin/api.py",
    "groupTitle": "Admin",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Id of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Name of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Email of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "username",
            "description": "<p>Username of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "Permission[]",
            "optional": false,
            "field": "permissions",
            "description": "<p>Permissions of admin</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "permissions.name",
            "description": "<p>Name of permission</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "permissions.access_level",
            "description": "<p>Access level of permission (None=0, Read=1, Write=2)</p>"
          },
          {
            "group": "Success Response",
            "type": "Permission[]",
            "optional": true,
            "field": "permissions.sub_permissions",
            "description": "<p>Sub permissions of permission</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Main",
    "name": "CheckToken",
    "type": "get",
    "url": "/v1/check_token",
    "title": "Check token exists or not",
    "filename": "./application/controllers/v1/main/api.py",
    "groupTitle": "Main",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Main",
    "name": "HealthCheck",
    "type": "get",
    "url": "/v1/health_check",
    "title": "Check health",
    "filename": "./application/controllers/v1/main/api.py",
    "groupTitle": "Main",
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 521": [
          {
            "group": "Error 521",
            "optional": false,
            "field": "Redis",
            "description": "<p>health check failed</p>"
          }
        ],
        "Error 522": [
          {
            "group": "Error 522",
            "optional": false,
            "field": "MongoDB",
            "description": "<p>health check failed</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Meeting",
    "name": "MeetingGetFile",
    "type": "post",
    "url": "/v1/meeting/:id/file/:type",
    "title": "Get meeting file",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired user</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "type",
            "description": "<p>Type of file</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/meeting/api.py",
    "groupTitle": "Meeting",
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Meeting",
    "name": "MeetingUploadFile",
    "type": "post",
    "url": "/v1/meeting/:id/file",
    "title": "Upload meeting file",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired meeting</p>"
          }
        ],
        "Form Parameter": [
          {
            "group": "Form Parameter",
            "type": "String",
            "optional": false,
            "field": "type",
            "description": "<p>File type</p>"
          },
          {
            "group": "Form Parameter",
            "type": "File",
            "optional": false,
            "field": "file",
            "description": "<p>File content, Max file size is 10MB</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/meeting/api.py",
    "groupTitle": "Meeting",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 201 Created",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Organization",
    "name": "ConfirmOrganization",
    "type": "post",
    "url": "/v1/organization/:id/confirm",
    "title": "Confirm organization",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired organization</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/organization/api.py",
    "groupTitle": "Organization",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Organization id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Organization email</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Organization name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "field_of_activity",
            "description": "<p>Organization field of activity</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "number_of_staff",
            "description": "<p>Organization number of staff</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "applied_before",
            "description": "<p>Organization applied before</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "manager_name",
            "description": "<p>Organization manager name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "operator_name",
            "description": "<p>Organization operator name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>Organization address</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "post_code",
            "description": "<p>Organization post code</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_tel",
            "description": "<p>Organization work tel</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_fax",
            "description": "<p>Organization home fax</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "purpose_for_taking_the_test",
            "description": "<p>Organization purpose for taking the test</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Organization more information</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_data",
            "description": "<p>Organization more data</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "balance",
            "description": "<p>Organization balance</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>Organization is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>Organization is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_confirmed",
            "description": "<p>Organization is confirmed or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Organization",
    "name": "CreateOrganizationPackage",
    "type": "post",
    "url": "/v1/organization/:id/package",
    "title": "Create a organization package",
    "filename": "./application/controllers/v1/organization/api.py",
    "groupTitle": "Organization",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "person",
            "description": "<p>Person email of the package</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "start_date",
            "description": "<p>Start date of the package (ISO format yyyy-mm-dd)</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "end_date",
            "description": "<p>End date of the package (ISO format yyyy-mm-dd)</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "budget",
            "description": "<p>Budget of the package</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Package id</p>"
          },
          {
            "group": "Success Response",
            "type": "Person",
            "optional": false,
            "field": "person",
            "description": "<p>Package person (<a href=\"#api-Person-GetPerson\">person object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "Person",
            "optional": false,
            "field": "organization",
            "description": "<p>Package organization (<a href=\"#api-Organization-GetOrganization\">organization object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "start_date",
            "description": "<p>Package start date</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "end_date",
            "description": "<p>Package end date</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "budget",
            "description": "<p>Package budget</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "balance",
            "description": "<p>Package balance</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 201 Created",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Organization",
    "name": "DeleteOrganizationPackage",
    "type": "delete",
    "url": "/v1/organization/:id/package/:package_id",
    "title": "Delete a organization package",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired organization</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "package_id",
            "description": "<p>ID of desired package</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/organization/api.py",
    "groupTitle": "Organization",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Organization",
    "name": "GetOrganization",
    "type": "get",
    "url": "/v1/organization/:id",
    "title": "Get a organization",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired organization</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/organization/api.py",
    "groupTitle": "Organization",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Organization id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Organization email</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Organization name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "field_of_activity",
            "description": "<p>Organization field of activity</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "number_of_staff",
            "description": "<p>Organization number of staff</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "applied_before",
            "description": "<p>Organization applied before</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "manager_name",
            "description": "<p>Organization manager name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "operator_name",
            "description": "<p>Organization operator name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>Organization address</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "post_code",
            "description": "<p>Organization post code</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_tel",
            "description": "<p>Organization work tel</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_fax",
            "description": "<p>Organization home fax</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "purpose_for_taking_the_test",
            "description": "<p>Organization purpose for taking the test</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Organization more information</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_data",
            "description": "<p>Organization more data</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "balance",
            "description": "<p>Organization balance</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>Organization is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>Organization is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_confirmed",
            "description": "<p>Organization is confirmed or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Organization",
    "name": "GetOrganizationList",
    "type": "get",
    "url": "/v1/organization",
    "title": "Get organization list",
    "parameter": {
      "fields": {
        "Query Parameter": [
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "email",
            "description": "<p>Filter by email</p>"
          },
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "is_confirmed",
            "description": "<p>Filter by is_confirmed field (true, false)</p>"
          }
        ],
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Current page</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "per_page",
            "defaultValue": "25",
            "description": "<p>Object per page (per_page = -1 return all)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Organization[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Organization-GetOrganization\">organization object</a></p>"
          }
        ],
        "Success - 2xx": [
          {
            "group": "Success - 2xx",
            "type": "Object",
            "optional": false,
            "field": "meta",
            "description": "<p>Pagination meta data.</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_next",
            "description": "<p>Pagination has next page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.next",
            "description": "<p>Url for next page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_prev",
            "description": "<p>Pagination has previous page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.prev",
            "description": "<p>Url for previous page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.page",
            "description": "<p>Number of the current page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.pages",
            "description": "<p>All pages count</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.per_page",
            "description": "<p>Item per each page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.total",
            "description": "<p>Count of all items</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/organization/api.py",
    "groupTitle": "Organization",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Organization",
    "name": "GetOrganizationPackage",
    "type": "get",
    "url": "/v1/organization/:id/package/:package_id",
    "title": "Get a organization package",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired organization</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "package_id",
            "description": "<p>ID of desired package</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/organization/api.py",
    "groupTitle": "Organization",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Package id</p>"
          },
          {
            "group": "Success Response",
            "type": "Person",
            "optional": false,
            "field": "person",
            "description": "<p>Package person (<a href=\"#api-Person-GetPerson\">person object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "Person",
            "optional": false,
            "field": "organization",
            "description": "<p>Package organization (<a href=\"#api-Organization-GetOrganization\">organization object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "start_date",
            "description": "<p>Package start date</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "end_date",
            "description": "<p>Package end date</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "budget",
            "description": "<p>Package budget</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "balance",
            "description": "<p>Package balance</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Organization",
    "name": "GetOrganizationPackageList",
    "type": "get",
    "url": "/v1/organization/:id/package",
    "title": "Get organization package list",
    "parameter": {
      "fields": {
        "Query Parameter": [
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "person",
            "description": "<p>Filter by person email</p>"
          }
        ],
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired organization</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Current page</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "per_page",
            "defaultValue": "25",
            "description": "<p>Object per page (per_page = -1 return all)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Package[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Organization-GetOrganizationPackage\">package object</a></p>"
          }
        ],
        "Success - 2xx": [
          {
            "group": "Success - 2xx",
            "type": "Object",
            "optional": false,
            "field": "meta",
            "description": "<p>Pagination meta data.</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_next",
            "description": "<p>Pagination has next page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.next",
            "description": "<p>Url for next page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_prev",
            "description": "<p>Pagination has previous page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.prev",
            "description": "<p>Url for previous page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.page",
            "description": "<p>Number of the current page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.pages",
            "description": "<p>All pages count</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.per_page",
            "description": "<p>Item per each page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.total",
            "description": "<p>Count of all items</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/organization/api.py",
    "groupTitle": "Organization",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Organization",
    "name": "GetOrganizationPerson",
    "type": "get",
    "url": "/v1/organization/:id/person/:person_id",
    "title": "Get a organization person",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired organization</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "person_id",
            "description": "<p>ID of desired person</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/organization/api.py",
    "groupTitle": "Organization",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Person id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Person email</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Person name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "first_name",
            "description": "<p>Person first name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "last_name",
            "description": "<p>Person last name</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "age",
            "description": "<p>Person age</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "sex",
            "description": "<p>Person sex</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "birth_date",
            "description": "<p>Person birth date</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "photo",
            "description": "<p>Person photo</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>Person address</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "post_code",
            "description": "<p>Person post code</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "mobile",
            "description": "<p>Person mobile</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_tel",
            "description": "<p>Person work tel</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "home_tel",
            "description": "<p>Person home tel</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "duration_of_hospitalization",
            "description": "<p>Person duration of hospitalization</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "illness_severity",
            "description": "<p>Person illness severity</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "disease_background",
            "description": "<p>Person disease background</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "family_disease_background",
            "description": "<p>Person family disease background</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "history_of_drug_use",
            "description": "<p>Person history of drug use</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "family_history_of_drug_use",
            "description": "<p>Person family history of drug use</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "birth_order",
            "description": "<p>Person birth order</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "number_of_children_in_family",
            "description": "<p>Person number of children in family</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Person more information</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>Person is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>Person is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Organization",
    "name": "GetOrganizationPersonDocument",
    "type": "get",
    "url": "/v1/organization/:id/person/:person_id/document/:document_id",
    "title": "Get a organization person document",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired organization</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "person_id",
            "description": "<p>ID of desired person</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "document_id",
            "description": "<p>ID of desired document</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/organization/api.py",
    "groupTitle": "Organization",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Document id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "type",
            "description": "<p>Document type (test=0, meeting=1)</p>"
          },
          {
            "group": "Success Response",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p>Document data</p>"
          },
          {
            "group": "Success Response",
            "type": "User",
            "optional": true,
            "field": "creator",
            "description": "<p>Document creator</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "creator.id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "creator.name",
            "description": "<p>User name</p>"
          },
          {
            "group": "Success Response",
            "type": "User",
            "optional": true,
            "field": "shared_with",
            "description": "<p>The document is shared with these users (owner only)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "shared_with.id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "shared_with.name",
            "description": "<p>User name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "create_time",
            "description": "<p>Document create time (ISO format yyyy-mm-ddThh:mm:ss)</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Organization",
    "name": "GetOrganizationPersonDocumentLit",
    "type": "get",
    "url": "/v1/organization/:id/person/:person_id/document",
    "title": "Get person document list",
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Document[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Organization-GetOrganizationPersonDocument\">document object</a></p>"
          }
        ],
        "Success - 2xx": [
          {
            "group": "Success - 2xx",
            "type": "Object",
            "optional": false,
            "field": "meta",
            "description": "<p>Pagination meta data.</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_next",
            "description": "<p>Pagination has next page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.next",
            "description": "<p>Url for next page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_prev",
            "description": "<p>Pagination has previous page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.prev",
            "description": "<p>Url for previous page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.page",
            "description": "<p>Number of the current page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.pages",
            "description": "<p>All pages count</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.per_page",
            "description": "<p>Item per each page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.total",
            "description": "<p>Count of all items</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired organization</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "person_id",
            "description": "<p>ID of desired person</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Current page</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "per_page",
            "defaultValue": "25",
            "description": "<p>Object per page (per_page = -1 return all)</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/organization/api.py",
    "groupTitle": "Organization",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Organization",
    "name": "GetOrganizationPersonList",
    "type": "get",
    "url": "/v1/organization/:id/person",
    "title": "Get organization person list",
    "parameter": {
      "fields": {
        "Query Parameter": [
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "person",
            "description": "<p>Filter by person email</p>"
          }
        ],
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired organization</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Current page</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "per_page",
            "defaultValue": "25",
            "description": "<p>Object per page (per_page = -1 return all)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Person[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Person-GetPerson\">person object</a></p>"
          }
        ],
        "Success - 2xx": [
          {
            "group": "Success - 2xx",
            "type": "Object",
            "optional": false,
            "field": "meta",
            "description": "<p>Pagination meta data.</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_next",
            "description": "<p>Pagination has next page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.next",
            "description": "<p>Url for next page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_prev",
            "description": "<p>Pagination has previous page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.prev",
            "description": "<p>Url for previous page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.page",
            "description": "<p>Number of the current page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.pages",
            "description": "<p>All pages count</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.per_page",
            "description": "<p>Item per each page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.total",
            "description": "<p>Count of all items</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/organization/api.py",
    "groupTitle": "Organization",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Organization",
    "name": "RejectOrganization",
    "type": "post",
    "url": "/v1/organization/:id/reject",
    "title": "Reject organization",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired organization</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/organization/api.py",
    "groupTitle": "Organization",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Organization id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Organization email</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Organization name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "field_of_activity",
            "description": "<p>Organization field of activity</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "number_of_staff",
            "description": "<p>Organization number of staff</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "applied_before",
            "description": "<p>Organization applied before</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "manager_name",
            "description": "<p>Organization manager name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "operator_name",
            "description": "<p>Organization operator name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>Organization address</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "post_code",
            "description": "<p>Organization post code</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_tel",
            "description": "<p>Organization work tel</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_fax",
            "description": "<p>Organization home fax</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "purpose_for_taking_the_test",
            "description": "<p>Organization purpose for taking the test</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Organization more information</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_data",
            "description": "<p>Organization more data</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "balance",
            "description": "<p>Organization balance</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>Organization is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>Organization is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_confirmed",
            "description": "<p>Organization is confirmed or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Organization",
    "name": "UpdateOrganization",
    "type": "put",
    "url": "/v1/organization/:id",
    "title": "Update a organization",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired organization</p>"
          }
        ],
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Name of the organization</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "field_of_activity",
            "description": "<p>Organization field of activity</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": false,
            "field": "number_of_staff",
            "description": "<p>Organization number of staff</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "applied_before",
            "description": "<p>Organization applied before</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "manager_name",
            "description": "<p>Organization manager name</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "operator_name",
            "description": "<p>Organization operator name</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "address",
            "description": "<p>Organization address</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "post_code",
            "description": "<p>Organization post code</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "work_tel",
            "description": "<p>Organization work tel</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "work_fax",
            "description": "<p>Organization home fax</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "purpose_for_taking_the_test",
            "description": "<p>Organization purpose for taking the test</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Organization more information</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "more_data",
            "description": "<p>Organization more data</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/organization/api.py",
    "groupTitle": "Organization",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Organization id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Organization email</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Organization name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "field_of_activity",
            "description": "<p>Organization field of activity</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "number_of_staff",
            "description": "<p>Organization number of staff</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "applied_before",
            "description": "<p>Organization applied before</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "manager_name",
            "description": "<p>Organization manager name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "operator_name",
            "description": "<p>Organization operator name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>Organization address</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "post_code",
            "description": "<p>Organization post code</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_tel",
            "description": "<p>Organization work tel</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_fax",
            "description": "<p>Organization home fax</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "purpose_for_taking_the_test",
            "description": "<p>Organization purpose for taking the test</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Organization more information</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_data",
            "description": "<p>Organization more data</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "balance",
            "description": "<p>Organization balance</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>Organization is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>Organization is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_confirmed",
            "description": "<p>Organization is confirmed or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "CreatePersonMeeting",
    "type": "post",
    "url": "/v1/person/:id/meeting",
    "title": "Create a person meeting",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          }
        ],
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "psychiatrist",
            "description": "<p>ID of desired psychiatrist</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "start_time",
            "description": "<p>Start time of the meeting (ISO format yyyy-mm-ddThh:mm:ss)</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": false,
            "field": "length",
            "description": "<p>Length of meeting (0=30min, 1=60min, 2=90min)</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Meeting id</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "person_accepted",
            "description": "<p>Person accepted or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "psychiatrist_accepted",
            "description": "<p>Psychiatrist accepted or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "status",
            "description": "<p>Meeting status (waiting=0, accepted=1, completed=2)</p>"
          },
          {
            "group": "Success Response",
            "type": "Person",
            "optional": false,
            "field": "person",
            "description": "<p>Meeting person (<a href=\"#api-Person-GetPerson\">person object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "Psychiatrist",
            "optional": false,
            "field": "psychiatrist",
            "description": "<p>Meeting psychiatrist (<a href=\"#api-Psychiatrist-GetPsychiatrist\">psychiatrist object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "result",
            "description": "<p>Meeting result</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "attachment",
            "description": "<p>Meeting attachment</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "score",
            "description": "<p>Meeting score</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "comment",
            "description": "<p>Meeting comment</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "price",
            "description": "<p>Meeting price</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "start_time",
            "description": "<p>Meeting start time</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "end_time",
            "description": "<p>Meeting end time</p>"
          },
          {
            "group": "Success Response",
            "type": "Document",
            "optional": false,
            "field": "health_test",
            "description": "<p>Person latest health test</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 201 Created",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "GetMeetingSuggestionForPerson",
    "type": "get",
    "url": "/v1/person/:id/meeting_suggestion",
    "title": "Get meeting suggestion for the person",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          }
        ],
        "Query Parameter": [
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": false,
            "field": "psychiatrist",
            "description": "<p>ID of psychiatrist</p>"
          },
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": false,
            "field": "start_date",
            "description": "<p>Start date</p>"
          },
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": false,
            "field": "end_date",
            "description": "<p>End date</p>"
          },
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": false,
            "field": "length",
            "description": "<p>Length (0=30min, 1=60min, 2=90min)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Object[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of time box array</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "list.date",
            "description": "<p>Desired date</p>"
          },
          {
            "group": "Success Response",
            "type": "TimeBox[]",
            "optional": false,
            "field": "list.time_boxes",
            "description": "<p>Time boxes</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "list.time_boxes.start_time",
            "description": "<p>Start of time box</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "list.time_boxes.length",
            "description": "<p>Length of time box (0=30min, 1=60min, 2=90min)</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "GetPerson",
    "type": "get",
    "url": "/v1/person/:id",
    "title": "Get a person",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Person id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Person email</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Person name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "first_name",
            "description": "<p>Person first name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "last_name",
            "description": "<p>Person last name</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "age",
            "description": "<p>Person age</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "sex",
            "description": "<p>Person sex</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "birth_date",
            "description": "<p>Person birth date</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "photo",
            "description": "<p>Person photo</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>Person address</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "post_code",
            "description": "<p>Person post code</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "mobile",
            "description": "<p>Person mobile</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_tel",
            "description": "<p>Person work tel</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "home_tel",
            "description": "<p>Person home tel</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "duration_of_hospitalization",
            "description": "<p>Person duration of hospitalization</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "illness_severity",
            "description": "<p>Person illness severity</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "disease_background",
            "description": "<p>Person disease background</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "family_disease_background",
            "description": "<p>Person family disease background</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "history_of_drug_use",
            "description": "<p>Person history of drug use</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "family_history_of_drug_use",
            "description": "<p>Person family history of drug use</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "birth_order",
            "description": "<p>Person birth order</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "number_of_children_in_family",
            "description": "<p>Person number of children in family</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Person more information</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>Person is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>Person is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "GetPersonDocument",
    "type": "get",
    "url": "/v1/person/:id/document/:document_id",
    "title": "Get a person document",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "document_id",
            "description": "<p>ID of desired document</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Document id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "type",
            "description": "<p>Document type (test=0, meeting=1)</p>"
          },
          {
            "group": "Success Response",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p>Document data</p>"
          },
          {
            "group": "Success Response",
            "type": "User",
            "optional": true,
            "field": "creator",
            "description": "<p>Document creator</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "creator.id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "creator.name",
            "description": "<p>User name</p>"
          },
          {
            "group": "Success Response",
            "type": "User",
            "optional": true,
            "field": "shared_with",
            "description": "<p>The document is shared with these users (owner only)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "shared_with.id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "shared_with.name",
            "description": "<p>User name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "create_time",
            "description": "<p>Document create time (ISO format yyyy-mm-ddThh:mm:ss)</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "GetPersonDocumentList",
    "type": "get",
    "url": "/v1/person/:id/document",
    "title": "Get person document list",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Current page</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "per_page",
            "defaultValue": "25",
            "description": "<p>Object per page (per_page = -1 return all)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Document[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Document-GetPersonDocument\">document object</a></p>"
          }
        ],
        "Success - 2xx": [
          {
            "group": "Success - 2xx",
            "type": "Object",
            "optional": false,
            "field": "meta",
            "description": "<p>Pagination meta data.</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_next",
            "description": "<p>Pagination has next page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.next",
            "description": "<p>Url for next page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_prev",
            "description": "<p>Pagination has previous page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.prev",
            "description": "<p>Url for previous page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.page",
            "description": "<p>Number of the current page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.pages",
            "description": "<p>All pages count</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.per_page",
            "description": "<p>Item per each page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.total",
            "description": "<p>Count of all items</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "GetPersonList",
    "type": "get",
    "url": "/v1/person",
    "title": "Get person list",
    "parameter": {
      "fields": {
        "Query Parameter": [
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "email",
            "description": "<p>Filter by email</p>"
          }
        ],
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Current page</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "per_page",
            "defaultValue": "25",
            "description": "<p>Object per page (per_page = -1 return all)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Person[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Person-GetPerson\">person object</a></p>"
          }
        ],
        "Success - 2xx": [
          {
            "group": "Success - 2xx",
            "type": "Object",
            "optional": false,
            "field": "meta",
            "description": "<p>Pagination meta data.</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_next",
            "description": "<p>Pagination has next page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.next",
            "description": "<p>Url for next page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_prev",
            "description": "<p>Pagination has previous page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.prev",
            "description": "<p>Url for previous page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.page",
            "description": "<p>Number of the current page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.pages",
            "description": "<p>All pages count</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.per_page",
            "description": "<p>Item per each page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.total",
            "description": "<p>Count of all items</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "GetPersonMeeting",
    "type": "get",
    "url": "/v1/person/:id/meeting/:meeting_id",
    "title": "Get a person meeting",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "meeting_id",
            "description": "<p>ID of desired meeting</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Meeting id</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "person_accepted",
            "description": "<p>Person accepted or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "psychiatrist_accepted",
            "description": "<p>Psychiatrist accepted or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "status",
            "description": "<p>Meeting status (waiting=0, accepted=1, completed=2)</p>"
          },
          {
            "group": "Success Response",
            "type": "Person",
            "optional": false,
            "field": "person",
            "description": "<p>Meeting person (<a href=\"#api-Person-GetPerson\">person object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "Psychiatrist",
            "optional": false,
            "field": "psychiatrist",
            "description": "<p>Meeting psychiatrist (<a href=\"#api-Psychiatrist-GetPsychiatrist\">psychiatrist object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "result",
            "description": "<p>Meeting result</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "attachment",
            "description": "<p>Meeting attachment</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "score",
            "description": "<p>Meeting score</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "comment",
            "description": "<p>Meeting comment</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "price",
            "description": "<p>Meeting price</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "start_time",
            "description": "<p>Meeting start time</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "end_time",
            "description": "<p>Meeting end time</p>"
          },
          {
            "group": "Success Response",
            "type": "Document",
            "optional": false,
            "field": "health_test",
            "description": "<p>Person latest health test</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "GetPersonMeetingList",
    "type": "get",
    "url": "/v1/person/:id/meeting",
    "title": "Get person meeting list",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Current page</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "per_page",
            "defaultValue": "25",
            "description": "<p>Object per page (per_page = -1 return all)</p>"
          }
        ],
        "Query Parameter": [
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "date",
            "description": "<p>Filter by date (ISO format yyyy-mm-dd)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Meeting[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Person-GetPersonMeeting\">meeting object</a></p>"
          }
        ],
        "Success - 2xx": [
          {
            "group": "Success - 2xx",
            "type": "Object",
            "optional": false,
            "field": "meta",
            "description": "<p>Pagination meta data.</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_next",
            "description": "<p>Pagination has next page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.next",
            "description": "<p>Url for next page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_prev",
            "description": "<p>Pagination has previous page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.prev",
            "description": "<p>Url for previous page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.page",
            "description": "<p>Number of the current page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.pages",
            "description": "<p>All pages count</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.per_page",
            "description": "<p>Item per each page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.total",
            "description": "<p>Count of all items</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "GetPersonOrganizationList",
    "type": "get",
    "url": "/v1/person/:id/organization",
    "title": "Get person organization list",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Organization[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Organization-GetOrganization\">organization object</a></p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "GetPersonPackage",
    "type": "get",
    "url": "/v1/person/:id/package/:package_id",
    "title": "Get a person package",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "package_id",
            "description": "<p>ID of desired package</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Package id</p>"
          },
          {
            "group": "Success Response",
            "type": "Person",
            "optional": false,
            "field": "person",
            "description": "<p>Package person (<a href=\"#api-Person-GetPerson\">person object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "Person",
            "optional": false,
            "field": "organization",
            "description": "<p>Package organization (<a href=\"#api-Organization-GetOrganization\">organization object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "start_date",
            "description": "<p>Package start date</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "end_date",
            "description": "<p>Package end date</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "budget",
            "description": "<p>Package budget</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "balance",
            "description": "<p>Package balance</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "GetPersonPackageList",
    "type": "get",
    "url": "/v1/person/:id/package",
    "title": "Get person package list",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Current page</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "per_page",
            "defaultValue": "25",
            "description": "<p>Object per page (per_page = -1 return all)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Package[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Person-GetPersonPackage\">package object</a></p>"
          }
        ],
        "Success - 2xx": [
          {
            "group": "Success - 2xx",
            "type": "Object",
            "optional": false,
            "field": "meta",
            "description": "<p>Pagination meta data.</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_next",
            "description": "<p>Pagination has next page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.next",
            "description": "<p>Url for next page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_prev",
            "description": "<p>Pagination has previous page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.prev",
            "description": "<p>Url for previous page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.page",
            "description": "<p>Number of the current page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.pages",
            "description": "<p>All pages count</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.per_page",
            "description": "<p>Item per each page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.total",
            "description": "<p>Count of all items</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "GetPsychiatristSuggestionForPerson",
    "type": "get",
    "url": "/v1/person/:id/psychiatrist_suggestion",
    "title": "Get psychiatrist suggestion for the person",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Psychiatrist[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Psychiatrist-GetPsychiatrist\">psychiatrist object</a></p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "SubmitPersonTest",
    "type": "get",
    "url": "/v1/person/:id/submit_test",
    "title": "Submit person test",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          }
        ],
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "Integer[]",
            "optional": false,
            "field": "choices",
            "description": "<p>Choices made for questions</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Document id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "type",
            "description": "<p>Document type (test=0, meeting=1)</p>"
          },
          {
            "group": "Success Response",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p>Document data</p>"
          },
          {
            "group": "Success Response",
            "type": "User",
            "optional": true,
            "field": "creator",
            "description": "<p>Document creator</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "creator.id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "creator.name",
            "description": "<p>User name</p>"
          },
          {
            "group": "Success Response",
            "type": "User",
            "optional": true,
            "field": "shared_with",
            "description": "<p>The document is shared with these users (owner only)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "shared_with.id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "shared_with.name",
            "description": "<p>User name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "create_time",
            "description": "<p>Document create time (ISO format yyyy-mm-ddThh:mm:ss)</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "UpdatePerson",
    "type": "put",
    "url": "/v1/person/:id",
    "title": "Update a person",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          }
        ],
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>Person first name</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>Person last name</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": false,
            "field": "age",
            "description": "<p>Person age</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": false,
            "field": "sex",
            "description": "<p>Person sex</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "birth_date",
            "description": "<p>Person birth date</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "photo",
            "description": "<p>Person photo</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>Person address</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "post_code",
            "description": "<p>Person post code</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "mobile",
            "description": "<p>Person mobile</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "work_tel",
            "description": "<p>Person work tel</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "home_tel",
            "description": "<p>Person home tel</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": false,
            "field": "duration_of_hospitalization",
            "description": "<p>Person duration of hospitalization</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "illness_severity",
            "description": "<p>Person illness severity</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "disease_background",
            "description": "<p>Person disease background</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "family_disease_background",
            "description": "<p>Person family disease background</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "history_of_drug_use",
            "description": "<p>Person history of drug use</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "family_history_of_drug_use",
            "description": "<p>Person family history of drug use</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": true,
            "field": "birth_order",
            "description": "<p>Person birth order</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": true,
            "field": "number_of_children_in_family",
            "description": "<p>Person number of children in family</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Person more information</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Person id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Person email</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Person name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "first_name",
            "description": "<p>Person first name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "last_name",
            "description": "<p>Person last name</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "age",
            "description": "<p>Person age</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "sex",
            "description": "<p>Person sex</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "birth_date",
            "description": "<p>Person birth date</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "photo",
            "description": "<p>Person photo</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>Person address</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "post_code",
            "description": "<p>Person post code</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "mobile",
            "description": "<p>Person mobile</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_tel",
            "description": "<p>Person work tel</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "home_tel",
            "description": "<p>Person home tel</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "duration_of_hospitalization",
            "description": "<p>Person duration of hospitalization</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "illness_severity",
            "description": "<p>Person illness severity</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "disease_background",
            "description": "<p>Person disease background</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "family_disease_background",
            "description": "<p>Person family disease background</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "history_of_drug_use",
            "description": "<p>Person history of drug use</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "family_history_of_drug_use",
            "description": "<p>Person family history of drug use</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "birth_order",
            "description": "<p>Person birth order</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "number_of_children_in_family",
            "description": "<p>Person number of children in family</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Person more information</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>Person is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>Person is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 409": [
          {
            "group": "Error 409",
            "optional": false,
            "field": "Conflict",
            "description": "<p>Indicates that the request could not be processed because of conflict in the request, such as an edit conflict between multiple simultaneous updates.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "UpdatePersonDocument",
    "type": "get",
    "url": "/v1/person/:id/document/:document_id",
    "title": "Update a person document",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "document_id",
            "description": "<p>ID of desired document</p>"
          }
        ],
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String[]",
            "optional": false,
            "field": "shared_with",
            "description": "<p>The document is shared with these users</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Document id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "type",
            "description": "<p>Document type (test=0, meeting=1)</p>"
          },
          {
            "group": "Success Response",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p>Document data</p>"
          },
          {
            "group": "Success Response",
            "type": "User",
            "optional": true,
            "field": "creator",
            "description": "<p>Document creator</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "creator.id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "creator.name",
            "description": "<p>User name</p>"
          },
          {
            "group": "Success Response",
            "type": "User",
            "optional": true,
            "field": "shared_with",
            "description": "<p>The document is shared with these users (owner only)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "shared_with.id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "shared_with.name",
            "description": "<p>User name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "create_time",
            "description": "<p>Document create time (ISO format yyyy-mm-ddThh:mm:ss)</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Person",
    "name": "UpdatePersonMeeting",
    "type": "put",
    "url": "/v1/person/:id/meeting/:meeting_id",
    "title": "Update a person meeting",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired person</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "meeting_id",
            "description": "<p>ID of desired meeting</p>"
          }
        ],
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "accepted",
            "description": "<p>Meeting accepted or not?</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": true,
            "field": "score",
            "description": "<p>Score of meeting (1-5)</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "comment",
            "description": "<p>Comment of meeting</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/person/api.py",
    "groupTitle": "Person",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Meeting id</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "person_accepted",
            "description": "<p>Person accepted or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "psychiatrist_accepted",
            "description": "<p>Psychiatrist accepted or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "status",
            "description": "<p>Meeting status (waiting=0, accepted=1, completed=2)</p>"
          },
          {
            "group": "Success Response",
            "type": "Person",
            "optional": false,
            "field": "person",
            "description": "<p>Meeting person (<a href=\"#api-Person-GetPerson\">person object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "Psychiatrist",
            "optional": false,
            "field": "psychiatrist",
            "description": "<p>Meeting psychiatrist (<a href=\"#api-Psychiatrist-GetPsychiatrist\">psychiatrist object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "result",
            "description": "<p>Meeting result</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "attachment",
            "description": "<p>Meeting attachment</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "score",
            "description": "<p>Meeting score</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "comment",
            "description": "<p>Meeting comment</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "price",
            "description": "<p>Meeting price</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "start_time",
            "description": "<p>Meeting start time</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "end_time",
            "description": "<p>Meeting end time</p>"
          },
          {
            "group": "Success Response",
            "type": "Document",
            "optional": false,
            "field": "health_test",
            "description": "<p>Person latest health test</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Psychiatrist",
    "name": "ConfirmPsychiatrist",
    "type": "post",
    "url": "/v1/psychiatrist/:id/confirm",
    "title": "Confirm psychiatrist",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired psychiatrist</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/psychiatrist/api.py",
    "groupTitle": "Psychiatrist",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Psychiatrist id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Psychiatrist email</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Psychiatrist name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "first_name",
            "description": "<p>Psychiatrist first name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "last_name",
            "description": "<p>Psychiatrist last name</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "score",
            "description": "<p>Psychiatrist score</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "age",
            "description": "<p>Psychiatrist age</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "sex",
            "description": "<p>Psychiatrist sex</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "birth_date",
            "description": "<p>Psychiatrist birth date</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "photo",
            "description": "<p>Psychiatrist photo</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>Psychiatrist address</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "post_code",
            "description": "<p>Psychiatrist post code</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "mobile",
            "description": "<p>Psychiatrist mobile</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_tel",
            "description": "<p>Psychiatrist work tel</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "home_tel",
            "description": "<p>Psychiatrist home tel</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "primary_credential",
            "description": "<p>Psychiatrist primary credential</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "primary_specialty",
            "description": "<p>Psychiatrist primary specialty</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "last_three_years_experiences",
            "description": "<p>Psychiatrist last three years experiences</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "name_of_posts_of_the_last_3_years",
            "description": "<p>Psychiatrist name of posts of the last 3 years</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "applied_before",
            "description": "<p>Psychiatrist applied before</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Psychiatrist more information</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_data",
            "description": "<p>Psychiatrist more data</p>"
          },
          {
            "group": "Success Response",
            "type": "Plan",
            "optional": true,
            "field": "plans",
            "description": "<p>Psychiatrist plans</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "plans.price",
            "description": "<p>Plan price</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>Psychiatrist is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>Psychiatrist is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_confirmed",
            "description": "<p>Psychiatrist is confirmed or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Psychiatrist",
    "name": "CreatePsychiatristMeeting",
    "type": "post",
    "url": "/v1/psychiatrist/:id/meeting",
    "title": "Create a psychiatrist meeting",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired psychiatrist</p>"
          }
        ],
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "person",
            "description": "<p>ID of desired person</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "start_time",
            "description": "<p>Start time of the meeting (ISO format yyyy-mm-ddThh:mm:ss)</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": false,
            "field": "length",
            "description": "<p>Length of meeting (0=30min, 1=60min, 2=90min)</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/psychiatrist/api.py",
    "groupTitle": "Psychiatrist",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Meeting id</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "person_accepted",
            "description": "<p>Person accepted or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "psychiatrist_accepted",
            "description": "<p>Psychiatrist accepted or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "status",
            "description": "<p>Meeting status (waiting=0, accepted=1, completed=2)</p>"
          },
          {
            "group": "Success Response",
            "type": "Person",
            "optional": false,
            "field": "person",
            "description": "<p>Meeting person (<a href=\"#api-Person-GetPerson\">person object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "Psychiatrist",
            "optional": false,
            "field": "psychiatrist",
            "description": "<p>Meeting psychiatrist (<a href=\"#api-Psychiatrist-GetPsychiatrist\">psychiatrist object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "result",
            "description": "<p>Meeting result</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "attachment",
            "description": "<p>Meeting attachment</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "score",
            "description": "<p>Meeting score</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "comment",
            "description": "<p>Meeting comment</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "price",
            "description": "<p>Meeting price</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "start_time",
            "description": "<p>Meeting start time</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "end_time",
            "description": "<p>Meeting end time</p>"
          },
          {
            "group": "Success Response",
            "type": "Document",
            "optional": false,
            "field": "health_test",
            "description": "<p>Person latest health test</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 201 Created",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Psychiatrist",
    "name": "CreatePsychiatristTimeBox",
    "type": "post",
    "url": "/v1/psychiatrist/:id/time_box",
    "title": "Create a psychiatrist time box",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired psychiatrist</p>"
          }
        ],
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "start_time",
            "description": "<p>Start time of the time box (ISO format yyyy-mm-ddThh:mm:ss)</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "end_time",
            "description": "<p>End time of the time box (ISO format yyyy-mm-ddThh:mm:ss)</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/psychiatrist/api.py",
    "groupTitle": "Psychiatrist",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>TimeBox id</p>"
          },
          {
            "group": "Success Response",
            "type": "Psychiatrist",
            "optional": false,
            "field": "psychiatrist",
            "description": "<p>Time box psychiatrist (<a href=\"#api-Psychiatrist-GetPsychiatrist\">psychiatrist object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "start_time",
            "description": "<p>TimeBox start time</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "end_time",
            "description": "<p>TimeBox end time</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 201 Created",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Psychiatrist",
    "name": "DeletePsychiatristTimeBox",
    "type": "delete",
    "url": "/v1/psychiatrist/:id/time_box/:time_box_id",
    "title": "Delete a psychiatrist time_box",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired psychiatrist</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "time_box_id",
            "description": "<p>ID of desired time box</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/psychiatrist/api.py",
    "groupTitle": "Psychiatrist",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Psychiatrist",
    "name": "GetPsychiatrist",
    "type": "get",
    "url": "/v1/psychiatrist/:id",
    "title": "Get a psychiatrist",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired psychiatrist</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/psychiatrist/api.py",
    "groupTitle": "Psychiatrist",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Psychiatrist id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Psychiatrist email</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Psychiatrist name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "first_name",
            "description": "<p>Psychiatrist first name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "last_name",
            "description": "<p>Psychiatrist last name</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "score",
            "description": "<p>Psychiatrist score</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "age",
            "description": "<p>Psychiatrist age</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "sex",
            "description": "<p>Psychiatrist sex</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "birth_date",
            "description": "<p>Psychiatrist birth date</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "photo",
            "description": "<p>Psychiatrist photo</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>Psychiatrist address</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "post_code",
            "description": "<p>Psychiatrist post code</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "mobile",
            "description": "<p>Psychiatrist mobile</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_tel",
            "description": "<p>Psychiatrist work tel</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "home_tel",
            "description": "<p>Psychiatrist home tel</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "primary_credential",
            "description": "<p>Psychiatrist primary credential</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "primary_specialty",
            "description": "<p>Psychiatrist primary specialty</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "last_three_years_experiences",
            "description": "<p>Psychiatrist last three years experiences</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "name_of_posts_of_the_last_3_years",
            "description": "<p>Psychiatrist name of posts of the last 3 years</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "applied_before",
            "description": "<p>Psychiatrist applied before</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Psychiatrist more information</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_data",
            "description": "<p>Psychiatrist more data</p>"
          },
          {
            "group": "Success Response",
            "type": "Plan",
            "optional": true,
            "field": "plans",
            "description": "<p>Psychiatrist plans</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "plans.price",
            "description": "<p>Plan price</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>Psychiatrist is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>Psychiatrist is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_confirmed",
            "description": "<p>Psychiatrist is confirmed or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Psychiatrist",
    "name": "GetPsychiatristList",
    "type": "get",
    "url": "/v1/psychiatrist",
    "title": "Get psychiatrist list",
    "parameter": {
      "fields": {
        "Query Parameter": [
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "email",
            "description": "<p>Filter by email</p>"
          },
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "is_confirmed",
            "description": "<p>Filter by is_confirmed field (true, false)</p>"
          }
        ],
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Current page</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "per_page",
            "defaultValue": "25",
            "description": "<p>Object per page (per_page = -1 return all)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Psychiatrist[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Psychiatrist-GetPsychiatrist\">psychiatrist object</a></p>"
          }
        ],
        "Success - 2xx": [
          {
            "group": "Success - 2xx",
            "type": "Object",
            "optional": false,
            "field": "meta",
            "description": "<p>Pagination meta data.</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_next",
            "description": "<p>Pagination has next page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.next",
            "description": "<p>Url for next page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_prev",
            "description": "<p>Pagination has previous page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.prev",
            "description": "<p>Url for previous page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.page",
            "description": "<p>Number of the current page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.pages",
            "description": "<p>All pages count</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.per_page",
            "description": "<p>Item per each page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.total",
            "description": "<p>Count of all items</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/psychiatrist/api.py",
    "groupTitle": "Psychiatrist",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Psychiatrist",
    "name": "GetPsychiatristMeeting",
    "type": "get",
    "url": "/v1/psychiatrist/:id/meeting/:meeting_id",
    "title": "Get a psychiatrist meeting",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired psychiatrist</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "meeting_id",
            "description": "<p>ID of desired meeting</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/psychiatrist/api.py",
    "groupTitle": "Psychiatrist",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Meeting id</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "person_accepted",
            "description": "<p>Person accepted or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "psychiatrist_accepted",
            "description": "<p>Psychiatrist accepted or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "status",
            "description": "<p>Meeting status (waiting=0, accepted=1, completed=2)</p>"
          },
          {
            "group": "Success Response",
            "type": "Person",
            "optional": false,
            "field": "person",
            "description": "<p>Meeting person (<a href=\"#api-Person-GetPerson\">person object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "Psychiatrist",
            "optional": false,
            "field": "psychiatrist",
            "description": "<p>Meeting psychiatrist (<a href=\"#api-Psychiatrist-GetPsychiatrist\">psychiatrist object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "result",
            "description": "<p>Meeting result</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "attachment",
            "description": "<p>Meeting attachment</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "score",
            "description": "<p>Meeting score</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "comment",
            "description": "<p>Meeting comment</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "price",
            "description": "<p>Meeting price</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "start_time",
            "description": "<p>Meeting start time</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "end_time",
            "description": "<p>Meeting end time</p>"
          },
          {
            "group": "Success Response",
            "type": "Document",
            "optional": false,
            "field": "health_test",
            "description": "<p>Person latest health test</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Psychiatrist",
    "name": "GetPsychiatristMeetingList",
    "type": "get",
    "url": "/v1/psychiatrist/:id/meeting",
    "title": "Get psychiatrist meeting list",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired psychiatrist</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Current page</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "per_page",
            "defaultValue": "25",
            "description": "<p>Object per page (per_page = -1 return all)</p>"
          }
        ],
        "Query Parameter": [
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "date",
            "description": "<p>Filter by date (ISO format yyyy-mm-dd)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "Meeting[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Psychiatrist-GetPsychiatristMeeting\">meeting object</a></p>"
          }
        ],
        "Success - 2xx": [
          {
            "group": "Success - 2xx",
            "type": "Object",
            "optional": false,
            "field": "meta",
            "description": "<p>Pagination meta data.</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_next",
            "description": "<p>Pagination has next page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.next",
            "description": "<p>Url for next page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_prev",
            "description": "<p>Pagination has previous page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.prev",
            "description": "<p>Url for previous page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.page",
            "description": "<p>Number of the current page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.pages",
            "description": "<p>All pages count</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.per_page",
            "description": "<p>Item per each page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.total",
            "description": "<p>Count of all items</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/psychiatrist/api.py",
    "groupTitle": "Psychiatrist",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Psychiatrist",
    "name": "GetPsychiatristTimeBox",
    "type": "get",
    "url": "/v1/psychiatrist/:id/time_box/:time_box_id",
    "title": "Get a psychiatrist time box",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired psychiatrist</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "time_box_id",
            "description": "<p>ID of desired time box</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/psychiatrist/api.py",
    "groupTitle": "Psychiatrist",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>TimeBox id</p>"
          },
          {
            "group": "Success Response",
            "type": "Psychiatrist",
            "optional": false,
            "field": "psychiatrist",
            "description": "<p>Time box psychiatrist (<a href=\"#api-Psychiatrist-GetPsychiatrist\">psychiatrist object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "start_time",
            "description": "<p>TimeBox start time</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "end_time",
            "description": "<p>TimeBox end time</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Psychiatrist",
    "name": "GetPsychiatristTimeBoxList",
    "type": "get",
    "url": "/v1/psychiatrist/:id/time_box",
    "title": "Get psychiatrist time box list",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired psychiatrist</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Current page</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "per_page",
            "defaultValue": "25",
            "description": "<p>Object per page (per_page = -1 return all)</p>"
          }
        ],
        "Query Parameter": [
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "date",
            "description": "<p>Filter by date (ISO format yyyy-mm-dd)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "TimeBox[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-Psychiatrist-GetPsychiatristTimeBox\">time box object</a></p>"
          }
        ],
        "Success - 2xx": [
          {
            "group": "Success - 2xx",
            "type": "Object",
            "optional": false,
            "field": "meta",
            "description": "<p>Pagination meta data.</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_next",
            "description": "<p>Pagination has next page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.next",
            "description": "<p>Url for next page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_prev",
            "description": "<p>Pagination has previous page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.prev",
            "description": "<p>Url for previous page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.page",
            "description": "<p>Number of the current page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.pages",
            "description": "<p>All pages count</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.per_page",
            "description": "<p>Item per each page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.total",
            "description": "<p>Count of all items</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/psychiatrist/api.py",
    "groupTitle": "Psychiatrist",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Psychiatrist",
    "name": "RejectPsychiatrist",
    "type": "post",
    "url": "/v1/psychiatrist/:id/reject",
    "title": "Reject psychiatrist",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired psychiatrist</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/psychiatrist/api.py",
    "groupTitle": "Psychiatrist",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Psychiatrist id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Psychiatrist email</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Psychiatrist name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "first_name",
            "description": "<p>Psychiatrist first name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "last_name",
            "description": "<p>Psychiatrist last name</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "score",
            "description": "<p>Psychiatrist score</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "age",
            "description": "<p>Psychiatrist age</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "sex",
            "description": "<p>Psychiatrist sex</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "birth_date",
            "description": "<p>Psychiatrist birth date</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "photo",
            "description": "<p>Psychiatrist photo</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>Psychiatrist address</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "post_code",
            "description": "<p>Psychiatrist post code</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "mobile",
            "description": "<p>Psychiatrist mobile</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_tel",
            "description": "<p>Psychiatrist work tel</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "home_tel",
            "description": "<p>Psychiatrist home tel</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "primary_credential",
            "description": "<p>Psychiatrist primary credential</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "primary_specialty",
            "description": "<p>Psychiatrist primary specialty</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "last_three_years_experiences",
            "description": "<p>Psychiatrist last three years experiences</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "name_of_posts_of_the_last_3_years",
            "description": "<p>Psychiatrist name of posts of the last 3 years</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "applied_before",
            "description": "<p>Psychiatrist applied before</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Psychiatrist more information</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_data",
            "description": "<p>Psychiatrist more data</p>"
          },
          {
            "group": "Success Response",
            "type": "Plan",
            "optional": true,
            "field": "plans",
            "description": "<p>Psychiatrist plans</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "plans.price",
            "description": "<p>Plan price</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>Psychiatrist is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>Psychiatrist is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_confirmed",
            "description": "<p>Psychiatrist is confirmed or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Psychiatrist",
    "name": "UpdatePsychiatrist",
    "type": "put",
    "url": "/v1/psychiatrist/:id",
    "title": "Update a psychiatrist",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired psychiatrist</p>"
          }
        ],
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>Psychiatrist first name</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>Psychiatrist last name</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": false,
            "field": "age",
            "description": "<p>Psychiatrist age</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": false,
            "field": "sex",
            "description": "<p>Psychiatrist sex</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "birth_date",
            "description": "<p>Psychiatrist birth date</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "photo",
            "description": "<p>Psychiatrist photo</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "address",
            "description": "<p>Psychiatrist address</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "post_code",
            "description": "<p>Psychiatrist post code</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "mobile",
            "description": "<p>Psychiatrist mobile</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "work_tel",
            "description": "<p>Psychiatrist work tel</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "home_tel",
            "description": "<p>Psychiatrist home tel</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": false,
            "field": "primary_credential",
            "description": "<p>Psychiatrist primary credential</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": false,
            "field": "primary_specialty",
            "description": "<p>Psychiatrist primary specialty</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "last_three_years_experiences",
            "description": "<p>Psychiatrist last three years experiences</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "name_of_posts_of_the_last_3_years",
            "description": "<p>Psychiatrist name of posts of the last 3 years</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "applied_before",
            "description": "<p>Psychiatrist applied before</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Psychiatrist more information</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "more_data",
            "description": "<p>Psychiatrist more data</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Plan[]",
            "optional": false,
            "field": "plans",
            "description": "<p>Psychiatrist plans</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Integer",
            "optional": true,
            "field": "plans.price",
            "description": "<p>Plan price</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/psychiatrist/api.py",
    "groupTitle": "Psychiatrist",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Psychiatrist id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Psychiatrist email</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Psychiatrist name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "first_name",
            "description": "<p>Psychiatrist first name</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "last_name",
            "description": "<p>Psychiatrist last name</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "score",
            "description": "<p>Psychiatrist score</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "age",
            "description": "<p>Psychiatrist age</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "sex",
            "description": "<p>Psychiatrist sex</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "birth_date",
            "description": "<p>Psychiatrist birth date</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "photo",
            "description": "<p>Psychiatrist photo</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>Psychiatrist address</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "post_code",
            "description": "<p>Psychiatrist post code</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "mobile",
            "description": "<p>Psychiatrist mobile</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "work_tel",
            "description": "<p>Psychiatrist work tel</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "home_tel",
            "description": "<p>Psychiatrist home tel</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "primary_credential",
            "description": "<p>Psychiatrist primary credential</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "primary_specialty",
            "description": "<p>Psychiatrist primary specialty</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "last_three_years_experiences",
            "description": "<p>Psychiatrist last three years experiences</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "name_of_posts_of_the_last_3_years",
            "description": "<p>Psychiatrist name of posts of the last 3 years</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "applied_before",
            "description": "<p>Psychiatrist applied before</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_information",
            "description": "<p>Psychiatrist more information</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": true,
            "field": "more_data",
            "description": "<p>Psychiatrist more data</p>"
          },
          {
            "group": "Success Response",
            "type": "Plan",
            "optional": true,
            "field": "plans",
            "description": "<p>Psychiatrist plans</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": true,
            "field": "plans.price",
            "description": "<p>Plan price</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>Psychiatrist is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>Psychiatrist is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_confirmed",
            "description": "<p>Psychiatrist is confirmed or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "Psychiatrist",
    "name": "UpdatePsychiatristMeeting",
    "type": "put",
    "url": "/v1/psychiatrist/:id/meeting/:meeting_id",
    "title": "Update a psychiatrist meeting",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired psychiatrist</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "meeting_id",
            "description": "<p>ID of desired meeting</p>"
          }
        ],
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "accepted",
            "description": "<p>Meeting accepted or not?</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "result",
            "description": "<p>Result of meeting</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": true,
            "field": "attachment",
            "description": "<p>Attachment of meeting</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/psychiatrist/api.py",
    "groupTitle": "Psychiatrist",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Meeting id</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "person_accepted",
            "description": "<p>Person accepted or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "psychiatrist_accepted",
            "description": "<p>Psychiatrist accepted or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "status",
            "description": "<p>Meeting status (waiting=0, accepted=1, completed=2)</p>"
          },
          {
            "group": "Success Response",
            "type": "Person",
            "optional": false,
            "field": "person",
            "description": "<p>Meeting person (<a href=\"#api-Person-GetPerson\">person object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "Psychiatrist",
            "optional": false,
            "field": "psychiatrist",
            "description": "<p>Meeting psychiatrist (<a href=\"#api-Psychiatrist-GetPsychiatrist\">psychiatrist object</a>)</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "result",
            "description": "<p>Meeting result</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "attachment",
            "description": "<p>Meeting attachment</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "score",
            "description": "<p>Meeting score</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "comment",
            "description": "<p>Meeting comment</p>"
          },
          {
            "group": "Success Response",
            "type": "Integer",
            "optional": false,
            "field": "price",
            "description": "<p>Meeting price</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "start_time",
            "description": "<p>Meeting start time</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "end_time",
            "description": "<p>Meeting end time</p>"
          },
          {
            "group": "Success Response",
            "type": "Document",
            "optional": false,
            "field": "health_test",
            "description": "<p>Person latest health test</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 201 Created",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "ActivateUser",
    "type": "post",
    "url": "/v1/user/activate",
    "title": "Activate a new user and get access token",
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "access_token",
            "description": ""
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "refresh_token",
            "description": ""
          },
          {
            "group": "Success Response",
            "type": "User",
            "optional": false,
            "field": "user",
            "description": "<p>User details (<a href=\"#api-User-GetUser\">User object</a>)</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "code",
            "description": "<p>Activation code for the user</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Email of the user</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "DisableUser",
    "type": "post",
    "url": "/v1/user/:id/disable",
    "title": "Disable user",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired user</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "role",
            "description": "<p>User role</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>User email</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>User is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>User is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "EnableUser",
    "type": "post",
    "url": "/v1/user/:id/enable",
    "title": "Enable user",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired user</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "role",
            "description": "<p>User role</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>User email</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>User is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>User is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "GetUser",
    "type": "get",
    "url": "/v1/user/:id",
    "title": "Get a user",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired user</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "role",
            "description": "<p>User role</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>User email</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>User is active or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_enable",
            "description": "<p>User is enable or not?</p>"
          },
          {
            "group": "Success Response",
            "type": "Boolean",
            "optional": true,
            "field": "is_profile_updated",
            "description": "<p>Has the user profile been updated or not?</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "GetUserList",
    "type": "get",
    "url": "/v1/user",
    "title": "Get user list",
    "parameter": {
      "fields": {
        "Query Parameter": [
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "role",
            "description": "<p>Filter by role</p>"
          },
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "query",
            "description": "<p>Filter by email (user)</p>"
          },
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "email",
            "description": "<p>Filter by email (admin)</p>"
          },
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "is_active",
            "description": "<p>Filter by is_active field (true, false)</p>"
          },
          {
            "group": "Query Parameter",
            "type": "String",
            "optional": true,
            "field": "is_enable",
            "description": "<p>Filter by is_enable field (true, false)</p>"
          }
        ],
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "page",
            "defaultValue": "1",
            "description": "<p>Current page</p>"
          },
          {
            "group": "URL Parameter",
            "type": "Integer",
            "optional": true,
            "field": "per_page",
            "defaultValue": "25",
            "description": "<p>Object per page (per_page = -1 return all)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "User[]",
            "optional": false,
            "field": "list",
            "description": "<p>List of <a href=\"#api-User-GetUser\">user object</a></p>"
          }
        ],
        "Success - 2xx": [
          {
            "group": "Success - 2xx",
            "type": "Object",
            "optional": false,
            "field": "meta",
            "description": "<p>Pagination meta data.</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_next",
            "description": "<p>Pagination has next page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.next",
            "description": "<p>Url for next page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Boolean",
            "optional": false,
            "field": "meta.has_prev",
            "description": "<p>Pagination has previous page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Url",
            "optional": true,
            "field": "meta.prev",
            "description": "<p>Url for previous page of results</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.page",
            "description": "<p>Number of the current page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.pages",
            "description": "<p>All pages count</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.per_page",
            "description": "<p>Item per each page</p>"
          },
          {
            "group": "Success - 2xx",
            "type": "Integer",
            "optional": false,
            "field": "meta.total",
            "description": "<p>Count of all items</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "RefreshToken",
    "type": "post",
    "url": "/v1/user/token/refresh",
    "title": "Refresh access token",
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "access_token",
            "description": "<p>Access token of user</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "refresh_token",
            "description": "<p>Refresh token for user</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "access_token",
            "description": "<p>Access token of the user</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "refresh_token",
            "description": "<p>Refresh token of the user</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "RegisterUser",
    "type": "post",
    "url": "/v1/user/register",
    "title": "Register a new user",
    "success": {
      "fields": {
        "Success Response": [
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "activate_ttl",
            "description": "<p>Activate token ttl</p>"
          },
          {
            "group": "Success Response",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Email of the user</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 201 Created",
          "type": "json"
        }
      ]
    },
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "role",
            "description": "<p>User role (person=0, psychiatrist=1, organization=2)</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Email of the user</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Password of the user (pattern='^[A-Za-z0-9]{8,}$')</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 409": [
          {
            "group": "Error 409",
            "optional": false,
            "field": "Conflict",
            "description": "<p>Indicates that the request could not be processed because of conflict in the request, such as an edit conflict between multiple simultaneous updates.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "RevokeAllTokens",
    "type": "delete",
    "url": "/v1/user/token/revoke_all",
    "title": "Revoke all access tokens",
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "RevokeToken",
    "type": "delete",
    "url": "/v1/user/token/revoke",
    "title": "Revoke access token",
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "SendActivateCodeJson",
    "type": "post",
    "url": "/v1/user/activate/code",
    "title": "Send new activation code to user",
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Email of the user</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>Password of the user (pattern='^[A-Za-z0-9]{8,}$')</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "UserChangePassword",
    "type": "put",
    "url": "/v1/user/password",
    "title": "Change user password",
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "old_password",
            "description": "<p>Old password of this user. (pattern='^[A-Za-z0-9]{8,}$')</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "new_password",
            "description": "<p>New password of this user. (pattern='^[A-Za-z0-9]{8,}$')</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "UserGetImage",
    "type": "post",
    "url": "/v1/user/:id/image/:type",
    "title": "Get user image",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired user</p>"
          },
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "type",
            "description": "<p>Type of image</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "UserRecoverPassword",
    "type": "put",
    "url": "/v1/user/password/recover",
    "title": "Request recover password",
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>User email</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "UserSetPassword",
    "type": "put",
    "url": "/v1/user/password/set",
    "title": "Set password by recover token",
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Content-Type",
            "description": "<p>JSON (application/json)</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "token",
            "description": "<p>Recover token</p>"
          },
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "new_password",
            "description": "<p>New password of this user. (pattern='^[A-Za-z0-9]{8,}$')</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ]
      }
    }
  },
  {
    "version": "1.0.0",
    "group": "User",
    "name": "UserUploadImage",
    "type": "post",
    "url": "/v1/user/:id/image",
    "title": "Upload user image",
    "parameter": {
      "fields": {
        "URL Parameter": [
          {
            "group": "URL Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>ID of desired user</p>"
          }
        ],
        "Form Parameter": [
          {
            "group": "Form Parameter",
            "type": "String",
            "optional": false,
            "field": "type",
            "description": "<p>File type</p>"
          },
          {
            "group": "Form Parameter",
            "type": "File",
            "optional": false,
            "field": "file",
            "description": "<p>File content, Max file size is 10MB</p>"
          }
        ]
      }
    },
    "filename": "./application/controllers/v1/user/api.py",
    "groupTitle": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Secret-Key",
            "description": "<p>Admin Request - Secret key for admin to use special APIs</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Access-Token",
            "description": "<p>User Request - Access token given after activation and refreshing</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Status Code",
          "content": "HTTP/1.1 201 Created",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 400": [
          {
            "group": "Error 400",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications.</p>"
          }
        ],
        "Error 401": [
          {
            "group": "Error 401",
            "optional": false,
            "field": "Unauthorized",
            "description": "<p>The request requires user authentication.</p>"
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "optional": false,
            "field": "Forbidden",
            "description": "<p>The server understood the request, but is refusing to fulfill it.</p>"
          }
        ],
        "Error 404": [
          {
            "group": "Error 404",
            "optional": false,
            "field": "NotFound",
            "description": "<p>The server has not found anything matching the Request-URI.</p>"
          }
        ]
      }
    }
  }
] });
