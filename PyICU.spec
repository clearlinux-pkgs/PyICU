#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyICU
Version  : 2.3.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/e9/35/211ffb949c68e688ade7d40426de030a24eaec4b6c45330eeb9c0285f43a/PyICU-2.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e9/35/211ffb949c68e688ade7d40426de030a24eaec4b6c45330eeb9c0285f43a/PyICU-2.3.1.tar.gz
Summary  : Python extension wrapping the ICU C++ API
Group    : Development/Tools
License  : MIT
Requires: PyICU-license = %{version}-%{release}
Requires: PyICU-python = %{version}-%{release}
Requires: PyICU-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : importlib_metadata
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pytest
BuildRequires : pytest-python
BuildRequires : wcwidth

%description
## Welcome
        
        Welcome to PyICU, a Python extension wrapping the ICU C++ libraries.
        
        ICU stands for "International Components for Unicode".
        These are the i18n libraries of the Unicode Consortium.
        They implement much of the Unicode Standard,
        many of its companion Unicode Technical Standards,
        and much of Unicode CLDR.

%package license
Summary: license components for the PyICU package.
Group: Default

%description license
license components for the PyICU package.


%package python
Summary: python components for the PyICU package.
Group: Default
Requires: PyICU-python3 = %{version}-%{release}
Provides: pyicu-python

%description python
python components for the PyICU package.


%package python3
Summary: python3 components for the PyICU package.
Group: Default
Requires: python3-core

%description python3
python3 components for the PyICU package.


%prep
%setup -q -n PyICU-2.3.1
cd %{_builddir}/PyICU-2.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576013677
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PyICU
cp %{_builddir}/PyICU-2.3.1/LICENSE %{buildroot}/usr/share/package-licenses/PyICU/30410e52eb79243849038655af921b51845dfed4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PyICU/30410e52eb79243849038655af921b51845dfed4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
