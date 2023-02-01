#
# spec file for package python-aws-xray-sdk
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%if 0%{?suse_version} >= 1550
%bcond_with aiobotocore
%else
%bcond_without aiobotocore
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-aws-xray-sdk
Version:        2.10.0
Release:        0
Summary:        The AWS X-Ray SDK for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/aws/aws-xray-sdk-python
Source:         https://github.com/aws/aws-xray-sdk-python/archive/refs/tags/%{version}.tar.gz#/aws-xray-sdk-python-%{version}-gh.tar.gz
Source9:        %{name}-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-botocore >= 1.11.3
Requires:       python-wrapt
%ifpython2
Requires:       python-future
%endif
%if %{with test}
BuildRequires:  %pythons
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module aws-xray-sdk = %{version}}
BuildRequires:  %{python_module aws-xray-sdk-Django = %{version}}
BuildRequires:  %{python_module aws-xray-sdk-Flask-SQLAlchemy = %{version}}
BuildRequires:  %{python_module aws-xray-sdk-SQLAlchemy = %{version}}
BuildRequires:  %{python_module aws-xray-sdk-aiohttp = %{version}}
BuildRequires:  %{python_module aws-xray-sdk-bottle = %{version}}
BuildRequires:  %{python_module aws-xray-sdk-mysql-connector = %{version}}
BuildRequires:  %{python_module aws-xray-sdk-psycopg2 = %{version}}
BuildRequires:  %{python_module aws-xray-sdk-pymongo = %{version}}
BuildRequires:  %{python_module aws-xray-sdk-pynamodb = %{version}}
BuildRequires:  %{python_module aws-xray-sdk-requests = %{version}}
BuildRequires:  %{python_module pytest-aiohttp}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
%if %{with aiobotocore}
BuildRequires:  %{python_module aws-xray-sdk-aiobotocore = %{version}}
%endif
%endif
BuildArch:      noarch
%python_subpackages

%description
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

It works through any one of various frameworks, provided by backends. The
following backends are included in the main package:

  * botocore
  * httplib
  * sqlite3

Additional backends can be installed by installing %{name}-backend
packages.  The %{name}-all package installs all backends.

%package        all
Summary:        Metapackage to pull in all AWS X-Ray SDK backends
Group:          Metapackages
Requires:       %{name} = %{version}
Recommends:     %{name}-Django = %{version}
Recommends:     %{name}-Flask-SQLAlchemy = %{version}
Recommends:     %{name}-SQLAlchemy = %{version}
Recommends:     %{name}-aiobotocore = %{version}
Recommends:     %{name}-aiohttp = %{version}
Recommends:     %{name}-bottle = %{version}
Recommends:     %{name}-mysql-connector = %{version}
Recommends:     %{name}-psycopg2 = %{version}
Recommends:     %{name}-pymongo = %{version}
Recommends:     %{name}-pynamodb = %{version}
Recommends:     %{name}-requests = %{version}

%description    all
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package pulls in all available backends for %{name}.

%package        Django
Summary:        Django backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-Django >= 1.10

%description    Django
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the Django backend for %{name}.

%package        Flask-SQLAlchemy
Summary:        Flask-SQLAlchemy backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       %{name}-SQLAlchemy = %{version}
Requires:       python-Flask-SQLAlchemy
Requires:       python-SQLAlchemy

%description    Flask-SQLAlchemy
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the Flask-SQLAlchemy backend for %{name}.

%package        SQLAlchemy
Summary:        SQLAlchemy backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-SQLAlchemy

%description    SQLAlchemy
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the SQLAlchemy backend for %{name}.

%package        bottle
Summary:        bottle backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-bottle >= 0.10

%description    bottle
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the bottle backend for %{name}.

%package        mysql-connector
Summary:        mysql backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-mysql-connector-python

%description    mysql-connector
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the mysql-connector-python backend for %{name}.

%package        pymongo
Summary:        pymongo backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-pymongo

%description    pymongo
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the pymongo backend for %{name}.

%package        pynamodb
Summary:        pynamodb backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-pynamodb >= 3.3.1

%description    pynamodb
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the pynamodb backend for %{name}.

%package        psycopg2
Summary:        psycopg2 backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-psycopg2

%description    psycopg2
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the psycopg2 backend for %{name}.

%package        requests
Summary:        requests backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-requests

%description    requests
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the requests backend for %{name}.

%package        aiobotocore
Summary:        aiobotocore backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-aiobotocore

%description    aiobotocore
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the aiobotocore backend for %{name}.

%package        aiohttp
Summary:        aiohttp backend for the AWS X-Ray Python SDK
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-aiohttp >= 3.0

%description    aiohttp
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.

This package provides the aiohttp backend for %{name}.

%prep
%setup -q -n aws-xray-sdk-python-%{version}

%if !%{with test}
%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export DJANGO_SETTINGS_MODULE=tests.ext.django.app.settings
export AWS_SECRET_ACCESS_KEY=fake_key
export AWS_ACCESS_KEY_ID=fake_id
%if !%{with aiobotocore}
ignore_tests+=" --ignore tests/ext/aiobotocore/test_aiobotocore.py"
%endif
#
# See tox.ini:
#
# incompatibe pytest-aiohttp
ignore_tests+=" --ignore tests/ext/aiohttp"
# not packaged
ignore_tests+=" --ignore tests/ext/pg8000/test_pg8000.py"
# no testing.postgresql package
ignore_tests+=" --ignore tests/ext/psycopg2/test_psycopg2.py"
ignore_tests+=" --ignore tests/ext/sqlalchemy_core/test_postgres.py"
# no testing.myssqld package
ignore_tests+=" --ignore tests/ext/pymysql/test_pymysql.py"
# no django-fake-model
ignore_tests+=" --ignore tests/ext/django"
# no connection to httpbin.org
ignore_tests+=" --ignore tests/ext/httplib/test_httplib.py"
ignore_tests+=" --ignore tests/ext/requests/test_requests.py"
# tests by connecting to live aws hosts
ignore_tests+=" --ignore tests/ext/pynamodb/test_pynamodb.py"
# https://github.com/aws/aws-xray-sdk-python/issues/321
python310_donttest=("-k" "not test_localstorage_isolation")
%pytest $ignore_tests "${$python_donttest[@]}"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/aws_xray_sdk
%{python_sitelib}/aws_xray_sdk-%{version}*-info
%exclude %{python_sitelib}/aws_xray_sdk/ext/aiohttp/
%exclude %{python_sitelib}/aws_xray_sdk/ext/aiobotocore/
%exclude %{python_sitelib}/aws_xray_sdk/ext/bottle/
%exclude %{python_sitelib}/aws_xray_sdk/ext/django/
%exclude %{python_sitelib}/aws_xray_sdk/ext/flask_sqlalchemy/
%exclude %{python_sitelib}/aws_xray_sdk/ext/mysql/
%exclude %{python_sitelib}/aws_xray_sdk/ext/psycopg2/
%exclude %{python_sitelib}/aws_xray_sdk/ext/pymongo/
%exclude %{python_sitelib}/aws_xray_sdk/ext/pynamodb/
%exclude %{python_sitelib}/aws_xray_sdk/ext/requests/
%exclude %{python_sitelib}/aws_xray_sdk/ext/sqlalchemy/

%files %{python_files all}
%license LICENSE

%files %{python_files Django}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/django/

%files %{python_files Flask-SQLAlchemy}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/flask_sqlalchemy/

%files %{python_files SQLAlchemy}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/sqlalchemy/

%files %{python_files bottle}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/bottle/

%files %{python_files mysql-connector}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/mysql/

%files %{python_files pymongo}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/pymongo/

%files %{python_files pynamodb}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/pynamodb/

%files %{python_files psycopg2}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/psycopg2/

%files %{python_files requests}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/requests/

%if %{with aiobotocore}
%files %{python_files aiobotocore}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/aiobotocore/
%endif

%files %{python_files aiohttp}
%license LICENSE
%{python_sitelib}/aws_xray_sdk/ext/aiohttp/
%endif

%changelog
