Summary:	C++ library for reading and writing Zip files
Summary(pl):	Biblioteka C++ do odczytu i zapisu plików Zip
Name:		zipios++
Version:	0.1.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/zipios/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
URL:		http://zipios.sourceforge.net/
BuildRequires:	zlib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zipios++ is a java.util.zip-like C++ library for reading and writing
Zip files. Access to individual entries is provided through standard
C++ iostreams. A simple read-only virtual file system that mounts
regular directories and zip files is also provided.

%description -l pl
Zipios++ jest jak java.util.zip bibliotek± C++ do odczytywania oraz
zapisywania plików Zip. Dostêp do pojedyñczych wpisów jest mo¿liwy
poprzed standardowe strumienie we/wy C++. Prosty wirtualny system
plików (tylko do odczytu) montuj±cy regularne katalogi oraz pliki zip
równie¿ jest dostarczany.

%package devel
Summary:	Header files for zipios++
Summary(pl):	Pliki nag³ówkowe zipios++
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	zlib-devel
Requires:	libstdc++-devel

%description devel
The header files are only needed for development of programs using the
zipios++.

%description devel -l pl
W pakiecie tym znajduj± siê pliki nag³ówkowe, przeznaczone dla
programistów u¿ywaj±cych bibliotek zipios++.

%package static
Summary:	Static zipios++ libraries
Summary(pl):	Biblioteki statyczne zipios++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static zipios++ libraries.

%description static -l pl
Biblioteki statyczne zipios++.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/zipios++

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
