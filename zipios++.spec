Summary:	C++ library for reading and writing Zip files
Summary(pl.UTF-8):	Biblioteka C++ do odczytu i zapisu plików Zip
Name:		zipios++
Version:	0.1.5
Release:	4
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/zipios/%{name}-%{version}.tar.gz
# Source0-md5:	da66383f6dd70b4766252fec3ff3d7bb
Patch0:		%{name}-shared.patch
Patch1:		%{name}-c++.patch
Patch2:		%{name}-gcc.patch
Patch3:		%{name}-gcc42.patch
URL:		http://zipios.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zipios++ is a java.util.zip-like C++ library for reading and writing
Zip files. Access to individual entries is provided through standard
C++ iostreams. A simple read-only virtual file system that mounts
regular directories and zip files is also provided.

%description -l pl.UTF-8
Zipios++ jest jak java.util.zip biblioteką C++ do odczytywania oraz
zapisywania plików Zip. Dostęp do pojedyńczych wpisów jest możliwy
poprzez standardowe strumienie we/wy C++. Prosty wirtualny system
plików (tylko do odczytu) montujący regularne katalogi oraz pliki zip
również jest dostarczany.

%package devel
Summary:	Header files for zipios++
Summary(pl.UTF-8):	Pliki nagłówkowe zipios++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	zlib-devel

%description devel
The header files are only needed for development of programs using the
zipios++.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone dla
programistów używających bibliotek zipios++.

%package static
Summary:	Static zipios++ libraries
Summary(pl.UTF-8):	Biblioteki statyczne zipios++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static zipios++ libraries.

%description static -l pl.UTF-8
Biblioteki statyczne zipios++.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/zipios++

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
