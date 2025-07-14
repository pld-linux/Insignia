Summary:	Insignia - DirectFB conformance test suite
Summary(pl.UTF-8):	Insignia - zbiór testów zgodności DirectFB
Name:		Insignia
Version:	1.0.4
Release:	1
License:	proprietary
Group:		Libraries
Source0:	http://www.directfb.org/downloads/Extras/%{name}-%{version}.tar.gz
# NoSource0-md5:	b16fdcbd9307710bda138223fba0a749
Patch0:		%{name}-c++.patch
NoSource:	0
URL:		http://www.directfb.org/
BuildRequires:	DirectFB-c++-devel >= 1:1.2.0
BuildRequires:	DirectFB-devel >= 1:1.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libpng-devel >= 2:1.2.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Insignia - DirectFB conformance test suite.

%description -l pl.UTF-8
Insignia - zbiór testów zgodności DirectFB.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# API not exported
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libinsignia.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/Insignia
%attr(755,root,root) %{_bindir}/InsigniaRun
%attr(755,root,root) %{_libdir}/libinsignia-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinsignia-1.0.so.4
%dir %{_libdir}/Insignia
%attr(755,root,root) %{_libdir}/Insignia/DFBTest*.Io
%{_datadir}/Insignia
