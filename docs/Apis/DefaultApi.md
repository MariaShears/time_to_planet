# DefaultApi

All URIs are relative to *http://time-to-planet-api.travisshears.xyz/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDuration**](DefaultApi.md#getDuration) | **GET** /planet/{planet} | Returns time in second to planet to send message to planet


<a name="getDuration"></a>
# **getDuration**
> Distance getDuration(planet)

Returns time in second to planet to send message to planet

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planet** | **String**| planet -- mars, venus, jupiter | [default to null]

### Return type

[**Distance**](..//Models/Distance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

