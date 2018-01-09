# Preface #

This document describes the functionality provided by the xlr-nuget-trigger-plugin.

See the **[XL Release Documentation](https://docs.xebialabs.com/xl-release/index.html)** for background information on XL Release and release concepts.

# CI status #

[![Build Status][xlr-nuget-trigger-plugin-travis-image] ][xlr-nuget-trigger-plugin-travis-url]
[![Codacy][xlr-nuget-trigger-plugin-codacy-image] ][xlr-nuget-trigger-plugin-codacy-url]
[![License: MIT][xlr-nuget-trigger-plugin-license-image] ][xlr-nuget-trigger-plugin-license-url]
[![Github All Releases][xlr-nuget-trigger-plugin-downloads-image] ]()

[xlr-nuget-trigger-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-nuget-trigger-plugin.svg?branch=master
[xlr-nuget-trigger-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-nuget-trigger-plugin
[xlr-nuget-trigger-plugin-codacy-image]: https://api.codacy.com/project/badge/Grade/b78313b1eb1b4b058dc4512b4d48c26f
[xlr-nuget-trigger-plugin-codacy-url]: https://www.codacy.com/app/rvanstone/xlr-nuget-trigger-plugin
[xlr-nuget-trigger-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xlr-nuget-trigger-plugin-license-url]: https://opensource.org/licenses/MIT
[xlr-nuget-trigger-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xlr-nuget-trigger-plugin/total.svg

# ALPHA WARNING - PLUGIN NOT RELEASED YET #

# Overview #

This plugin is a XL Release plugin that enables triggering new releases based on a new NuGet package version showing up.

## Installation ##

Place the latest released version under the `plugins` subdirectory in the XL Release installation directory.

This plugin requires XLR 6.0.x+

## Testing ##

### Start containers for testing ###

Once you have all prerequisies, run `./gradlew runDockerCompose` to spin up an XL Release conainer with this plugin (+ test data loaded).

### Finish XL Release test setup ###

Now open up XL Release (see docker-compose.yml which port, but at time of writing localhost:15516) go into Design > Templates, find the `registry-triggered-template` and click on it, navigate to Triggers in the white dropdown (renders default with 'Release Flow').

For NuGet Server docs and commands, see [here](https://docs.microsoft.com/en-us/nuget/api/search-query-service-resource)
