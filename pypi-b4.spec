#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-b4
Version  : 0.12.3
Release  : 3
URL      : https://files.pythonhosted.org/packages/8c/bc/841866057347310e38865341b973727bb99558a26e7eae4b7e00b6c5a886/b4-0.12.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/8c/bc/841866057347310e38865341b973727bb99558a26e7eae4b7e00b6c5a886/b4-0.12.3.tar.gz
Summary  : A tool to work with public-inbox and patch archives
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: pypi-b4-bin = %{version}-%{release}
Requires: pypi-b4-license = %{version}-%{release}
Requires: pypi-b4-man = %{version}-%{release}
Requires: pypi-b4-python = %{version}-%{release}
Requires: pypi-b4-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
B4 tools
========
This is a helper utility to work with patches made available via a
public-inbox archive like lore.kernel.org. It is written to make it
easier to participate in a patch-based workflows, like those used in
the Linux kernel development.

%package bin
Summary: bin components for the pypi-b4 package.
Group: Binaries
Requires: pypi-b4-license = %{version}-%{release}

%description bin
bin components for the pypi-b4 package.


%package license
Summary: license components for the pypi-b4 package.
Group: Default

%description license
license components for the pypi-b4 package.


%package man
Summary: man components for the pypi-b4 package.
Group: Default

%description man
man components for the pypi-b4 package.


%package python
Summary: python components for the pypi-b4 package.
Group: Default
Requires: pypi-b4-python3 = %{version}-%{release}

%description python
python components for the pypi-b4 package.


%package python3
Summary: python3 components for the pypi-b4 package.
Group: Default
Requires: python3-core
Provides: pypi(b4)
Requires: pypi(dkimpy)
Requires: pypi(dnspython)
Requires: pypi(git_filter_repo)
Requires: pypi(patatt)
Requires: pypi(requests)

%description python3
python3 components for the pypi-b4 package.


%prep
%setup -q -n b4-0.12.3
cd %{_builddir}/b4-0.12.3
pushd ..
cp -a b4-0.12.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687795478
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-b4
cp %{_builddir}/b4-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-b4/4cc77b90af91e615a64ae04893fdffa7939db84c || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/b4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-b4/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/b4.5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
