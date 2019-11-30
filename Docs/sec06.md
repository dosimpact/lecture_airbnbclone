# section 06

# 6.0 Room Admin Panel

[참조 문서 ](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)

- list_display 인스턴스들 표시 | list_filter 인스턴스 필터 | search_fields 인스턴스 검색 | fields
- host--외래키 참조할때, model에서는 .으로 했는데, model.admin에서는 -- 로 참조.

```cs
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )
    list_filter = ("instant_book", "city", "country")
    search_fields = ("=city", "^host__username") # 완전일치 | 외래키 참조 + 시작 일치.

```

```cs
Prefix	Lookup
^	startswith
=	iexact
@	search
None	icontains
```

# 6.1 Room Admin Panel part Two (11:29)

# 6.2 Custom Admin Functions (6:08)
