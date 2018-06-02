Summary:  A C library for parsing/normalizing street addresses
Name: libpostal
Version: 1.0.0
Release: 2%{?dist}
License: MIT
Group: Development/Libraries
URL: https://github.com/openvenues/libpostal

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: libtool

%description
A C library for parsing/normalizing street addresses around the world


%package devel
Summary: libpostal development headers and static library
Group: Development/Libraries

%description devel
A C library for parsing/normalizing street addresses around the world.
This package provides libraries and headers for development

%prep
%setup -q -n %{name}-%{version}

%build
%{__make} clean || true

CFLAGS="$CFLAGS -fPIC -lstdc++"
CXXFLAGS="$CXXFLAGS -fPIC"
./bootstrap.sh

CONFEXTRA=""

%ifarch armv7hl
CONFEXTRA="--with-cflags-scanner-extra=-marm --disable-sse2"
%endif

%configure --datadir=/usr/local/libpostal/data --disable-data-download $CONFEXTRA

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%pre

%post

%files
%defattr(-, root, root, 0755)
%{_bindir}/libpostal_data
%{_libdir}/libpostal*.so*


%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libpostal
%{_libdir}/libpostal.a
%{_libdir}/pkgconfig/libpostal.pc

%changelog
* Sat Jun 02 2018 Martin Kolman <martin.kolman@gmail.com> - 1.0.0-2
- initial Fedora packaging

* Fri May 18 2018 rinigus <rinigus.git@gmail.com> - 1.0.0-1
- update to 1.0 libpostal

* Wed Jan 18 2017 rinigus <rinigus.git@gmail.com> - 0.3.3-1
- initial packaging release for SFOS
